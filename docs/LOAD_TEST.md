# Part 3 - Load Test (QuickPizza, HTTPS)

## How to run

```bash
cd part3-load
pip install -r requirements.txt
python run_load_test.py          # about 1 minute: probe before, 1000 users, probe after
```

Results are written to `part3-load/reports/`:

| File | Content |
|---|---|
| `summary.md` | before / during / after response times and Locust totals |
| `locust_report.html` | Locust HTML report with charts |
| `locust_stats.csv`, `locust_stats_history.csv` | raw numbers, per second during the run |
| `responses.txt` | full headers and timing of the analysed responses |

To run only the load, without the probe: `python -m locust -f locustfile.py --headless -u 1000 -r 66.67 -t 20s`.
To watch it live in the Locust web UI: `python -m locust -f locustfile.py`, then open http://localhost:8089.
The target, user count and ramp time can be changed in `.env` (see `.env.example`).

The run documented below is saved in [docs/evidence/](evidence/): [part3-summary.md](evidence/part3-summary.md), [part3-locust-report.html](evidence/part3-locust-report.html), [part3-responses.txt](evidence/part3-responses.txt).

## 1. The test in detail

### Target
**https://quickpizza.grafana.com** is Grafana's public demo app, built for people to practise load testing on. A load test sends a lot of traffic, so it should only run against a site that allows it. Running one against any random site without permission can look like an attack. QuickPizza is a SvelteKit front end served by a Go backend behind an AWS Application Load Balancer.

### Tool
**Locust 2.32** (Python), so Part 3 uses the same language as Parts 1 and 2. Locust sends real HTTPS requests, and each virtual user is a small Python class. I used `FastHttpUser` (geventhttpclient) because it can run 1000 users on one laptop.

### Scenario: 1000 users visit the homepage within 15 seconds

| Setting | Value | Why |
|---|---|---|
| Users | 1000 | from the assignment |
| Spawn rate | 66.67 users/s (1000 / 15) | arrivals are spread evenly over the 15 s |
| Visits per user | exactly 1 | `wait_time = constant(3600)`, so after its visit a user stays idle until the end |
| Run time | 20 s | the 15 s ramp plus 5 s so the last visits can finish |
| Request | `GET /` with `Accept: text/html` over HTTPS | the homepage document |
| Connection | new TCP + TLS connection per user | each user acts like a new visitor, not a reused connection |
| Check | status 200 **and** body contains `<title>QuickPizza</title>` | an error page that comes back as 200 still counts as a failure |

So the load is 1000 arrivals at about 67 per second, and **not** 1000 users all connected at the same moment. By Little's law, about 67 req/s × about 1.07 s per request means roughly 70 requests are in flight at any time.

Only the HTML document is requested. A real browser would also load about 16 JS chunks, one CSS file and the icon, so roughly 20 requests per visit. The assignment asks for the homepage, and it's the one request that every visit always makes.

### Measuring response time before, during and after
`run_load_test.py` runs a **separate single-user probe** next to Locust:

1. **Before:** 10 homepage requests, 0.5 s apart, while nothing else is running. This is the baseline.
2. **During:** Locust runs in a subprocess while the probe keeps sending one request every 0.5 s.
3. **After:** 10 more probe requests, to check that the app recovered.

The probe uses a fresh httpx client for each sample, so every sample includes DNS, TCP, TLS and the request, the same as a new visitor. It's a steady "one real user" gauge. The Locust numbers come from inside the load generator, which is busy creating 1000 connections, so they also include some overhead on our side.

### A problem in the load generator, found and fixed
In the first 1000-user run, Locust recorded **0 completed requests** and warned that CPU was above 90%. The cause was on our side. For every new user, geventhttpclient built a new TLS context and loaded all the CA certificates (on Windows this includes the system certificate store). At 67 new users per second, that CPU work starved the event loop, so no request finished.

The fix in [locustfile.py](../part3-load/locustfile.py): build one verified TLS context once and share it. Each user still does its own full TLS handshake. After the fix, CPU stayed normal and 1000 of 1000 requests completed. This is a reminder to check the load generator's own health (CPU, errors) before trusting the numbers.

## 2. Results (run on 2026-10-01, 12:51 UTC, from Bangalore)

### Single-user probe (ms)

| Phase | Samples | Errors | Min | Median | Avg | p95 | Max |
|---|---|---|---|---|---|---|---|
| Before | 10 | 0 | 761 | 805 | 818 | 964 | 964 |
| During | 14 | 0 | 754 | 803 | 799 | 828 | 853 |
| After | 10 | 0 | 773 | 819 | 825 | 911 | 911 |

### Locust, all 1000 visits (ms)

| Requests | Failures | Median | Avg | p95 | p99 | Max | Throughput |
|---|---|---|---|---|---|---|---|
| 1000 | 0 (0%) | 1100 | 1074 | 1100 | 1200 | 1231 | 66 req/s at full ramp |

Locust rounds percentiles to 2 significant figures, so 1100 means about 1050 to 1149.

Response time over the run, from `locust_stats_history.csv`:

| Second | Users | Completed requests | Median | p95 |
|---|---|---|---|---|
| 2 | 198 | 66 | 1100 | 1100 |
| 5 | 396 | 269 | 1100 | 1100 |
| 9 | 660 | 528 | 1100 | 1100 |
| 13 | 924 | 792 | 1100 | 1100 |
| 15 | 1000 | 988 | 1100 | 1100 |

## 3. Did the load test affect response time?

**No measurable impact.**

- Probe median: **805 ms before, 803 ms during, 819 ms after**. The 2 to 16 ms differences are smaller than normal network jitter (single samples range from 754 to 964 ms in every phase). The p95 during the load (828 ms) was actually lower than before (964 ms), which shows those differences are noise.
- Locust's median and p95 stayed flat at 1100 ms from the first user to the 1000th. Response time did not rise as users were added.
- Throughput kept up with the arrival rate (about 66 req/s), so requests were not queuing.
- 0 errors in all 1034 requests (1000 load + 34 probe).

**Why:** 67 requests per second for a 2.8 KB static HTML file is a light load for a Go server behind an AWS load balancer. Almost all of the response time is network distance, not server work. Timing from curl, Bangalore to the AWS host (one of its addresses, 18.119.85.144, is in the us-east-2 / Ohio range):

| Phase | Time |
|---|---|
| DNS | ~10 ms |
| TCP connect (1 round trip) | ~265 ms |
| TLS 1.3 handshake (1 round trip) | ~270 ms |
| Request to first byte (1 round trip) | ~250 ms |
| **Total for a new visitor** | **~800 ms** |

One network round trip is about 255 ms, and a new visitor needs three of them. That leaves the server only about 0 to 15 ms of work per request. On a reused (keep-alive) connection the same request takes about **250 ms**, which is one round trip.

The Locust median (about 1070 ms) is about 270 ms higher than the probe. A 5-user run was no faster (1245 to 2085 ms), so the gap comes from the load generator (Python TLS in gevent on Windows), not from load on the server.

**Limits of this result:**
- It was one run from one laptop on one network.
- 1000 arrivals over 15 s is a fairly gentle arrival rate. To find the breaking point, increase the rate step by step (for example 100, 250, 500 and 1000 req/s), or hold 1000 concurrent users with `wait_time = between(1, 3)`. Run Locust on several machines with `--master` / `--worker` so the generator itself doesn't become the bottleneck.
- Only the HTML document was tested. Static assets, the `/api/pizza` endpoint and the database behind it were not.

## 4. What is a good response time for a modern web app?

There isn't one number. It depends on what you measure:

| Metric | Good target | Source |
|---|---|---|
| Server response time (backend work) | **< 200 ms** | Google PageSpeed "Reduce server response times" |
| Time to First Byte (TTFB) as the user sees it | **≤ 800 ms** good, > 1800 ms poor (at p75) | web.dev TTFB |
| API calls (JSON) | p95 **< 200 to 300 ms**, p99 < 1 s | common SLO practice |
| Largest Contentful Paint (page looks loaded) | **≤ 2.5 s** at p75 | Core Web Vitals |
| Interaction to Next Paint (page reacts to a click) | **≤ 200 ms** at p75 | Core Web Vitals |
| How users feel it | 0.1 s feels instant, 1 s keeps their flow, 10 s and they leave | Nielsen Norman Group |

A practical target: the homepage HTML returns within **200 ms of server time** and within **800 ms TTFB at p75** for real users, and the full page loads within **2.5 s**. Look at percentiles (p95/p99), not averages, because users notice the slowest requests.

**QuickPizza against these targets:** the server itself is fast (about 0 to 15 ms of work). From India, though, the TTFB for a new visitor is about 800 ms, which is right at the "good" limit. Almost all of it is the distance to the US. A CDN or edge cache would bring the HTML and static files close to the user.

## 5. Analysis of HTTP/S responses

Captured with `run_load_test.py` (full output in [part3-responses.txt](evidence/part3-responses.txt)) and curl.

### 5.1 Homepage: `GET /`
```
HTTP/1.1 200 OK  (281 ms on a reused connection, 2847 bytes)
content-type: text/html; charset=utf-8
content-length: 2847
connection: keep-alive
set-cookie: AWSALB=...; Expires=+7 days; Path=/, AWSALBCORS=...; Path=/; SameSite=None; Secure
accept-ranges: bytes
vary: Origin
```
- **200 OK** with the right `text/html; charset=utf-8` and a fixed `content-length`, so the response isn't chunked. The body is a small SvelteKit shell that preloads 16 JS modules.
- **`connection: keep-alive`**: the connection can be reused. That's why a second request takes about 250 ms instead of about 800 ms.
- **`set-cookie: AWSALB / AWSALBCORS`**: AWS ALB sticky-session cookies. They tell us the stack (AWS Application Load Balancer) and pin each client to one backend instance. `AWSALB` has no `Secure` or `HttpOnly` flag. The ALB sets these cookies itself.
- **No `Server` header**: good, the server software and version aren't exposed.
- **No `Cache-Control`, `ETag` or `Last-Modified`**: browsers have no caching rule and can't make a conditional request (`304 Not Modified`), so every visit downloads the page again in full.
- **No security headers**: there's no `Strict-Transport-Security`, `Content-Security-Policy`, `X-Frame-Options` or `X-Content-Type-Options` on the HTML. Without HSTS, a first visit to `http://` can be downgraded.

### 5.2 Homepage with `Accept-Encoding: gzip, br`
```
HTTP/1.1 200 OK  (264 ms, 2847 bytes)
content-length: 2847        <- same size, no content-encoding header
```
- **No compression.** The client said it accepts gzip and brotli, but the server sent the same 2847 bytes with no `Content-Encoding`. For this small page the cost is small. The 16 KB CSS file and the JS bundles also go out uncompressed, though, and gzip would usually cut text like this by 60 to 80%.

### 5.3 Static asset: `GET /_app/immutable/assets/0.kLK4yNcK.css`
```
HTTP/1.1 200 OK  (527 ms, 16151 bytes)
content-type: text/css; charset=utf-8
content-length: 16151
set-cookie: AWSALB=...
```
- The file name has a content hash, and the path even says `immutable`, but there's **no `Cache-Control: public, max-age=31536000, immutable`**. Returning visitors download every asset again. This is the biggest easy improvement for a real user's page load time.
- Sticky-session cookies on a static file aren't needed, and `Set-Cookie` stops most shared caches and CDNs from caching the response.
- It takes 527 ms against 264 ms for the HTML on the same connection: 16 KB needs more TCP round trips on a 255 ms path while the connection is still ramping up its send rate.

### 5.4 Missing page: `GET /this-page-does-not-exist`
```
HTTP/1.1 404 Not Found  (331 ms, 19 bytes)
content-type: text/plain; charset=utf-8
x-content-type-options: nosniff
body: 404 page not found
```
- The status code is correct (a real 404, not a "soft 404" with status 200).
- The body is Go's default `404 page not found` in plain text, not a styled app page with a link back home. That's poor UX for a user who follows a broken link.
- `x-content-type-options: nosniff` is set here but not on the HTML homepage, so security headers are inconsistent across responses.

### 5.5 Protocol and connection
- **TLS 1.3**, and the server offers **HTTP/2** through ALPN (`h2`). Locust and httpx used HTTP/1.1. A browser would use HTTP/2 and load the 20 or so homepage files over one connection.
- The DNS name resolves to two IP addresses (load balancer nodes).
- Connection setup (TCP + TLS) is about **2/3 of a new visitor's response time** (about 535 of 800 ms). Keep-alive, HTTP/2 and a closer edge (CDN) would cut that the most. A faster server would barely change it.

### Summary of findings

| # | Finding | Impact | Fix |
|---|---|---|---|
| 1 | No compression (gzip/brotli) | larger downloads for CSS/JS | turn on compression at the ALB or app |
| 2 | No `Cache-Control` on hashed `/_app/immutable/` assets | repeat visits download everything again | `Cache-Control: public, max-age=31536000, immutable` |
| 3 | No CDN, all traffic goes to us-east-2 | ~800 ms TTFB from Asia | CloudFront or another CDN in front of the ALB |
| 4 | No HSTS / CSP / X-Frame-Options on HTML | weaker protection against HTTPS downgrade, clickjacking and XSS | add security headers |
| 5 | Sticky-session cookies on every response, including static files and 404s | stops shared caching, `AWSALB` has no `Secure` flag | turn off stickiness if it isn't needed, or limit it to API paths |
| 6 | Plain-text Go 404 page | poor UX on broken links | serve the app's own 404 page |
