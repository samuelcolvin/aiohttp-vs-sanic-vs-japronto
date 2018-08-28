# Requirements

python 3.6, postgres, `pip install -U aiohttp uvloop ujson asyncpg sanic japronto`

# Benchmarks

## aiohttp

version: `3.4.0`

```
➤  wrk -d 60 -c 2000 -t 12 --timeout 8 http://localhost:8000  # aiohttp
Running 1m test @ http://localhost:8000
  12 threads and 2000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    72.02ms   20.86ms   1.01s    97.21%
    Req/Sec     1.16k   653.88     3.83k    63.73%
  829953 requests in 1.00m, 132.18MB read
  Socket errors: connect 983, read 6443, write 0, timeout 0
Requests/sec:  13820.94
Transfer/sec:      2.20MB

➤  wrk -d 60 -c 2000 -t 12 --timeout 8 http://localhost:8000/db  # aiohttp
Running 1m test @ http://localhost:8000/db
  12 threads and 2000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   571.84ms    1.11s    7.99s    87.45%
    Req/Sec   237.39    125.57     1.16k    69.98%
  170071 requests in 1.00m, 31.05MB read
  Socket errors: connect 983, read 5582220, write 0, timeout 283
Requests/sec:   2831.93
Transfer/sec:    529.47KB
```

## sanic

version: `0.7.0`

```
➤  wrk -d 60 -c 2000 -t 12 --timeout 8 http://localhost:8000  # sanic
Running 1m test @ http://localhost:8000
  12 threads and 2000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    34.35ms   28.43ms   1.74s    99.81%
    Req/Sec     2.48k   849.25     5.86k    57.85%
  1776795 requests in 1.00m, 228.76MB read
  Socket errors: connect 983, read 13636, write 0, timeout 0
Requests/sec:  29583.17
Transfer/sec:      3.81MB

➤  wrk -d 60 -c 2000 -t 12 --timeout 8 http://localhost:8000/db  # sanic
Running 1m test @ http://localhost:8000/db
  12 threads and 2000 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.16s     1.86s    8.00s    83.82%
    Req/Sec    71.41    166.42     1.40k    94.10%
  25076 requests in 1.00m, 3.82MB read
  Socket errors: connect 983, read 12316451, write 0, timeout 1876
Requests/sec:    417.31
Transfer/sec:     65.05KB
```

## japronto

version: `japronto==0.1.1`

Doesn't seem to work with my setup, I get a lot of 
`SystemError: NULL result without error in PyObject_Call` and no results from wrk.


# Versions Details

updated on 28th August 2018

```
➤  python -V
Python 3.6.5
```

```
➤  pip freeze
aiofiles==0.4.0
aiohttp==3.4.0
async-timeout==3.0.0
asyncpg==0.17.0
attrs==18.1.0
chardet==3.0.4
httptools==0.0.11
idna==2.7
idna-ssl==1.1.0
japronto==0.1.1
multidict==4.3.1
pkg-resources==0.0.0
sanic==0.7.0
ujson==1.35
uvloop==0.11.2
websockets==6.0
yarl==1.2.6
```

```
➤  psql -U postgres -h localhost -c 'SELECT version()'
PostgreSQL 10.5 (Ubuntu 10.5-0ubuntu0.18.04) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 7.3.0-16ubuntu3) 7.3.0, 64-bit
```

```
➤  wrk --version
wrk 4.0.2 [epoll] Copyright (C) 2012 Will Glozer
```
