# Curl

## :

`Curl` at first glance a simple util to make HTTP request, but it is an important util to troubleshouting for me.

## Examples:

### Check TCP port is open on target host:
```sh
$ curl telnet://google.com:443 -v

*   Trying 142.250.185.174:443...
* Connected to google.com (142.250.185.174) port 443
``` 
> Util `telnet` don't require to installed.
