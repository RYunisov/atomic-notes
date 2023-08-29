# SS

Network util to investigate sockets.

That util as alternative to `netstat`. Because the last is depricated.

# Tips

Sometimes the faster way to find which a service listen port.

```bash
# ss -panl | grep 4422

tcp   LISTEN 0   128   0.0.0.0:4422   0.0.0.0:*   users:(("docker-proxy",pid=266142,fd=4))
```

That means the service docker-proxy binds a port 4422 and PID is 266142.

Show all `LISTING` socket

> `root` permission isn't require

```bash
$ ss -tul
```

Show all `LISTING` socket and process

> It is require `root` permission

```bash
# ss -tupl
```

Calculate and sort type of connections

```bash
# ss -tan | awk {'print $1'} | cut -d: -f1 | sort | uniq -c | sort -n
```

Show count of requests by IP_ADDR

```bash
# ss -tan | grep EST | grep <IP_ADDR> | wc -l
```

Show count of requests by IP_ADDR. The same as above with different output.

```bash
# ss -tan | grep EST | grep <IP_ADDR> | awk '{ print $5 }' | tr ":" " " | awk '{ print $1 }' | sort | uniq -c
```
