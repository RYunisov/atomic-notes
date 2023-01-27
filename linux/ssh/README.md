# SSH

## Tips

### Generate key

```bash
$ ssh-keygen -t ed25519
```

### Copy a generated key into a target host

```bash
$ ssh-copyid -l <username> <target_host>
```

### Connect to host through load-balancer

* Load Balancer have to know about HostSNI which passing in request;
* Resolve will be running on Load Balancer side;
* Source host might carreless about `target_host` FQDN.

Scheme:

```mermaid
flowchart LR
    A[User] -->|TCP/443| C(LoadBalancer)
    C -->|TCP/22| D[SSH]
```

```bash
$ ssh -o "ProxyCommand=openssl s_client -quiet -servername %h -connect <loadbalancer_host>:<loadbalancer_port>" <target_host> 
```

### Make a tunnel between source host and target

Imagine a situation on `target_host` exists to running a process on loopback interface, which not availabled outside.

```bash
$ ss -tanpl | grep 127.0.0.1

LISTEN  0        1024           127.0.0.1:8080          0.0.0.0:*
```

We can make to able reacheble from `source_host` thought ssh util.

```bash
$ ssh -L 127.0.0.1:8080:8080 <target_host>
```
