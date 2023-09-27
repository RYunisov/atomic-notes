# SSH

## Tips

### Static config

Util `ssh` able to using predefined configurations.
The most popular place to check `~/.ssh/config`, `/etc/ssh/ssh_config`

Example:

```bash
Host baloo
   Hostname <hostname>
   Port <port>
   User <username>
   LocalForward 3000 localhost:3000
   LocalForward 8080 localhost:8080
   LocalForward 4646 localhost:4646
   LocalForward 9090 localhost:9090
   ForwardAgent yes

```

Hostname `baloo` like an alias will using to connect via SSH.

```bash
$ ssh baloo
```

### Generate key

```bash
$ ssh-keygen -t ed25519
```

### Copy a generated key into a target host

```bash
$ ssh-copyid -l <username> <target_host>
```

### Connect to host through LoadBalancer

* LoadBalancer have to know about HostSNI which passing in request;
* Resolve will be running on LoadBalancer side;
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

### How to transfer files through SSH connection

Basically `rsync` or `scp` can transfer data through SSH connection.
However in case when just pure SSH you also can doing that.

Transfer files from localhost to the remote host
```bash
$ tar -czf - <SRC_FOLDER> | ssh <REMOTE_HOST> tar -xzf - -C <DEST_FOLDER>
```

Transfer data from the remote host on localhost
```bash
$ ssh <REMOTE_HOST> tar -czf - <SRC_FOLDER> | tar -xzf - -C <DEST_FOLDER>
```

# ssh-agent

The util `ssh-agent` provide to make easy process to forward auth through other host/hosts.

```bash
$ eval (ssh-add)              # Sometime requires to use `eval` to init ssh-agent
$ ssh-add                     # Add key to ssh agent
$ ssh-add -L                  # Check already added keys
$ ssh <target_host> -A        # Enable Agent-Forwarding(On target host also have to enabled)
<target_host> $ ssh-add -L    # Check already added keys on target host after login on target host
$ env | grep SSH_AUTH_SOCK    # Place where storing ssh-agent sock
```

