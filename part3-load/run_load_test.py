"""Runs the whole Part 3 scenario and writes reports/summary.md.

1. before: single-user probe, PROBE_SAMPLES homepage requests
2. during: Locust ramps LOAD_USERS visitors over LOAD_RAMP_SECONDS while the probe keeps measuring
3. after:  the probe measures again, to see if the app recovered
4. saves a few full HTTP responses (headers + timing) for analysis
"""
import csv
import statistics
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone

import httpx

import config

HEADERS = {"User-Agent": config.USER_AGENT}


def probe_once():
    # a fresh client per request, so each sample pays DNS + TCP + TLS like a new visitor
    with httpx.Client(headers=HEADERS, timeout=config.REQUEST_TIMEOUT) as client:
        start = time.perf_counter()
        try:
            resp = client.get(config.LOAD_BASE_URL + "/")
            ok = resp.status_code == 200
        except httpx.HTTPError:
            ok = False
        return (time.perf_counter() - start) * 1000, ok


def probe(samples):
    results = []
    for _ in range(samples):
        results.append(probe_once())
        time.sleep(config.PROBE_INTERVAL)
    return results


def probe_until(stop_event, results):
    while not stop_event.is_set():
        results.append(probe_once())
        time.sleep(config.PROBE_INTERVAL)


def percentile(values, pct):
    values = sorted(values)
    index = max(0, round(pct / 100 * len(values)) - 1)
    return values[index]


def summarize(results):
    times = [ms for ms, _ in results]
    return {
        "samples": len(results),
        "errors": sum(1 for _, ok in results if not ok),
        "min": min(times),
        "median": statistics.median(times),
        "avg": statistics.mean(times),
        "p95": percentile(times, 95),
        "max": max(times),
    }


def run_locust():
    spawn_rate = round(config.LOAD_USERS / config.LOAD_RAMP_SECONDS, 2)
    run_time = int(config.LOAD_RAMP_SECONDS) + config.LOAD_GRACE_SECONDS
    cmd = [
        sys.executable, "-m", "locust", "-f", "locustfile.py", "--headless",
        "--users", str(config.LOAD_USERS),
        "--spawn-rate", str(spawn_rate),
        "--run-time", f"{run_time}s",
        "--html", str(config.REPORTS_DIR / "locust_report.html"),
        "--csv", str(config.REPORTS_DIR / "locust"),
        "--only-summary",
    ]
    print("running:", " ".join(cmd[2:]))
    return subprocess.run(cmd, cwd=config.REPORTS_DIR.parent).returncode, spawn_rate, run_time


def locust_totals():
    with open(config.REPORTS_DIR / "locust_stats.csv", newline="") as f:
        for row in csv.DictReader(f):
            if row["Name"] == "Aggregated":
                return row
    return {}


def capture_responses():
    """A few full responses to analyse: the page, a static asset, a missing page."""
    with httpx.Client(headers=HEADERS, timeout=config.REQUEST_TIMEOUT) as client:
        home = client.get(config.LOAD_BASE_URL + "/")
        css = next((part.split('"')[0] for part in home.text.split('href="./')[1:] if ".css" in part.split('"')[0]), None)
        targets = [("Homepage", "/"), ("Homepage, gzip accepted", "/")]
        if css:
            targets.append(("Static asset (CSS)", "/" + css))
        targets.append(("Missing page", "/this-page-does-not-exist"))

        lines = []
        for title, path in targets:
            extra = {"Accept-Encoding": "gzip, br"} if "gzip" in title else {"Accept-Encoding": "identity"}
            resp = client.get(config.LOAD_BASE_URL + path, headers=extra)
            lines.append(f"### {title}: GET {path}")
            lines.append(f"{resp.http_version} {resp.status_code} {resp.reason_phrase}"
                         f"  ({resp.elapsed.total_seconds() * 1000:.0f} ms, {len(resp.content)} bytes decoded)")
            lines += [f"{k}: {v}" for k, v in resp.headers.items()]
            lines.append("")
        return "\n".join(lines)


def row(name, s):
    return (f"| {name} | {s['samples']} | {s['errors']} | {s['min']:.0f} | {s['median']:.0f} | "
            f"{s['avg']:.0f} | {s['p95']:.0f} | {s['max']:.0f} |")


def main():
    config.REPORTS_DIR.mkdir(exist_ok=True)
    started = datetime.now(timezone.utc)

    print(f"before: {config.PROBE_SAMPLES} probe requests to {config.LOAD_BASE_URL}")
    before = probe(config.PROBE_SAMPLES)

    print(f"during: {config.LOAD_USERS} users over {config.LOAD_RAMP_SECONDS:g}s")
    during, stop = [], threading.Event()
    prober = threading.Thread(target=probe_until, args=(stop, during))
    prober.start()
    exit_code, spawn_rate, run_time = run_locust()
    stop.set()
    prober.join()

    print("after: probe again")
    after = probe(config.PROBE_SAMPLES)

    responses = capture_responses()
    (config.REPORTS_DIR / "responses.txt").write_text(responses, encoding="utf-8")

    b, d, a = summarize(before), summarize(during), summarize(after)
    load = locust_totals()
    summary = f"""# Load test summary

- Target: {config.LOAD_BASE_URL}/
- Started: {started:%Y-%m-%d %H:%M:%S} UTC
- Load: {config.LOAD_USERS} users, spawn rate {spawn_rate}/s (ramp {config.LOAD_RAMP_SECONDS:g}s), run time {run_time}s
- Locust exit code: {exit_code} (0 = no failed requests)

## Single-user probe (ms)

| Phase | Samples | Errors | Min | Median | Avg | p95 | Max |
|---|---|---|---|---|---|---|---|
{row("Before", b)}
{row("During", d)}
{row("After", a)}

Median during vs before: {d['median'] / b['median']:.2f}x, p95 during vs before: {d['p95'] / b['p95']:.2f}x

## Locust, all {load.get('Request Count', '?')} visits (ms)

| Requests | Failures | Median | Avg | p95 | p99 | Max | Req/s |
|---|---|---|---|---|---|---|---|
| {load.get('Request Count')} | {load.get('Failure Count')} | {load.get('50%')} | {float(load.get('Average Response Time', 0)):.0f} | {load.get('95%')} | {load.get('99%')} | {float(load.get('Max Response Time', 0)):.0f} | {float(load.get('Requests/s', 0)):.1f} |

Full report: locust_report.html. Raw responses: responses.txt.
"""
    (config.REPORTS_DIR / "summary.md").write_text(summary, encoding="utf-8")
    print(summary)
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
