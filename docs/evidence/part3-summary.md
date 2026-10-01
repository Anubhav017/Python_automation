# Load test summary

- Target: https://quickpizza.grafana.com/
- Started: 2026-10-01 12:51:32 UTC
- Load: 1000 users, spawn rate 66.67/s (ramp 15s), run time 20s
- Locust exit code: 0 (0 = no failed requests)

## Single-user probe (ms)

| Phase | Samples | Errors | Min | Median | Avg | p95 | Max |
|---|---|---|---|---|---|---|---|
| Before | 10 | 0 | 761 | 805 | 818 | 964 | 964 |
| During | 14 | 0 | 754 | 803 | 799 | 828 | 853 |
| After | 10 | 0 | 773 | 819 | 825 | 911 | 911 |

Median during vs before: 1.00x, p95 during vs before: 0.86x

## Locust, all 1000 visits (ms)

| Requests | Failures | Median | Avg | p95 | p99 | Max | Req/s |
|---|---|---|---|---|---|---|---|
| 1000 | 0 | 1100 | 1074 | 1100 | 1200 | 1231 | 62.4 |

Full report: locust_report.html. Raw responses: responses.txt.
