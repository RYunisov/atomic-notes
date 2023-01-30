# Iptables

## Brief

`iptables` is statefull firewall util. Also it can use for redirect network trafic.
Don't forget to read a manual `man iptables`

> Require `root` permissions

## Tips

Show all rules in all chains in `filter` table

```bash
# iptables -nL
```

Show all rules in INPUT chain in `nat` table

```bash
# iptables -nL INPUT -t nat
```

Add rule in INPUT chain in `filter` table

```bash
# iptables -A INPUT -i ens160 -p tcp -m tcp --dport 53 -j ACCEPT
```

Add a new rule in specify line in chain

```bash
# iptables -I INPUT 1 -i ens160 -p tcp -m tcp --dport 53 -j ACCEPT
```

Update a general policy(ACCEPT or DROP) for specific chain

```bash
# iptables -P INPUT DROP
```

