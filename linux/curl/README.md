# Curl

## Description:

`Curl` at first glance a simple util to make HTTP request, but it is an powerfull util to troubleshouting.

## Examples:

### Check TCP port is open on target host:
```sh
$ curl telnet://github.com:443 -v

*   Trying 140.82.121.4:443...
* Connected to google.com (140.82.121.4) port 443
``` 
> Util `telnet` don't require to installed.

### Make request with manual DNS resolve

```sh
$ curl -v --resolve github.com:8443:127.0.0.1 https://github.com:8443

* Added github.com:8443:127.0.0.1 to DNS cache
* Hostname github.com was found in DNS cache
*   Trying 127.0.0.1:8443...
* connect to 127.0.0.1 port 8443 failed: Connection refused
* Failed to connect to github.com port 8443 after 0 ms: Connection refused
* Closing connection 0
curl: (7) Failed to connect to github.com port 8443 after 0 ms: Connection refused
```
> `Curl` can make to resolve without asking DNS server or `/etc/hosts`