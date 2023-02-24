# Sshuttle

It is perfect util if you want to forward traffic through ssh tunnel without pain.

Install:

```bash
$ pip install sshuttle
```

Tips:

* Run as daemon and forward traffic for 192.168.10.0/16 subnet though ssh host

```bash
# Require `root` permission

# sshuttle -r <user>@<host> 192.168.10.0/16 --daemon
```

# How it works underhood

Util `sshuttle` create iptables rules in different tables and linux kernel operate next steps.
