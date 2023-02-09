# Dig

DNS util provides huge actions to check domain service.

## Tips

* Return from PTR record to domain name

Example will be return ip - 216.239.32.10 to ns1.google.com

```bash
$ dig -x 216.239.32.10

; <<>> DiG 9.10.6 <<>> -x 216.239.32.10
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6569
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;10.32.239.216.in-addr.arpa.	IN	PTR

;; ANSWER SECTION:
10.32.239.216.in-addr.arpa. 57143 IN	PTR	ns1.google.com.

;; Query time: 30 msec
;; SERVER: 192.168.178.1#53(192.168.178.1)
;; WHEN: Thu Feb 09 23:11:42 CET 2023
;; MSG SIZE  rcvd: 83
```

* Make resolve from specific DNS

Example shows as make request through 8.8.8.8.

```bash
$ dig @8.8.8.8 github.com

; <<>> DiG 9.10.6 <<>> @8.8.8.8 github.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 55555
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;github.com.			IN	A

;; ANSWER SECTION:
github.com.		60	IN	A	140.82.121.3

;; Query time: 34 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Thu Feb 09 23:14:51 CET 2023
;; MSG SIZE  rcvd: 55
```
