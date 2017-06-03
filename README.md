# Requirements

python 3.6, postgres, `pip install aiohttp uvloop ujson asyncpg sanic japronto`


# aiohttp

```
➤ wrk -d 10 -c 100 -t 12 --timeout 8 http://localhost:8000  # aiohttp
Running 10s test @ http://localhost:8000
  12 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.52ms    1.58ms  43.44ms   93.29%
    Req/Sec   594.37     48.42   646.00     81.33%
  71051 requests in 10.01s, 11.32MB read
Requests/sec:   7099.30
Transfer/sec:      1.13MB
➤ wrk -d 10 -c 100 -t 12 --timeout 8 http://localhost:8000/db  # aiohttp
Running 10s test @ http://localhost:8000/db
  12 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    27.43ms    6.93ms 151.69ms   97.44%
    Req/Sec   296.99     24.29   340.00     87.14%
  35327 requests in 10.01s, 6.46MB read
Requests/sec:   3528.96
Transfer/sec:    661.25KB
```

# sanic

```
➤ wrk -d 10 -c 100 -t 12 --timeout 8 http://localhost:8000  # sanic
Running 10s test @ http://localhost:8000
  12 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     4.55ms  724.50us  17.67ms   94.63%
    Req/Sec     1.77k   499.35    18.67k    98.92%
  211459 requests in 10.10s, 27.43MB read
Requests/sec:  20936.08
Transfer/sec:      2.72MB
➤ wrk -d 10 -c 100 -t 12 --timeout 8 http://localhost:8000/db  # sanic
Running 10s test @ http://localhost:8000/db
  12 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    16.98ms    6.05ms 124.18ms   98.70%
    Req/Sec   483.90     40.57   540.00     94.46%
  57605 requests in 10.01s, 8.82MB read
Requests/sec:   5755.33
Transfer/sec:      0.88MB
```

# japronto

```
➤  wrk -d 10 -c 100 -t 12 --timeout 8 http://localhost:8000  # japonto
Running 10s test @ http://localhost:8000
  12 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     0.97ms  170.55us   8.80ms   96.13%
    Req/Sec     8.32k   705.14    12.87k    93.96%
  999654 requests in 10.10s, 100.10MB read
Requests/sec:  98983.65
Transfer/sec:      9.91MB
➤  wrk -d 10 -c 100 -t 12 --timeout 8 http://localhost:8000/db  # japonto
Running 10s test @ http://localhost:8000/db
  12 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.38ms  286.86us  18.92ms   94.50%
    Req/Sec     3.66k     2.21k    7.37k    54.73%
  73169 requests in 10.10s, 11.30MB read
Requests/sec:   7246.00
Transfer/sec:      1.12MB
```
