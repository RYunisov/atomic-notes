# Tcpdump

## Brief

`tcpdump` is a great util for dump and capture a network traffik
Require `root` permissions to run and assign network interfaces

## Tips

* Capture network traffic and filtering just 80 port in ALL interfaces

```bash
# tcpdump -npi any port 80
```

* Carture network traffic and filter just destination 53 port in ALL interfaces

```bash
# tcpdump -npi any dst port 53
```
