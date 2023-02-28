# nc

ncat is simple util for troubleshouting network

Tips:

* Starting listing any port

> Don't forget if you want to use port less 1024 range, it is require `root` permission

```bash
$ nc --listen 4096
```

* Check available port in target host

```bash
$ nc -vz <target_host> <target_port>
```

