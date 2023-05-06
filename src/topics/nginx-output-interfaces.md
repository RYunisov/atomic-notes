# Nginx output through different interfaces

Sometime we faced with different challenges and most important think
it implements that as soon is possible and more elegance.

Imagine a situation, we have just only one interface for incoming requests
and you need to use other interfaces just for output traffic.

Nginx have it out of box.

Scheme like that:

```
->  192.168.1.99
X   192.168.1.10 ->
X   192.168.1.20 ->
X   192.168.1.30 ->
```

* Usually `nginx` exists module as `ngx_http_split_clients_module`
* Configure `nginx` add block with `split_clients`

```
split_clients "$request_uri$remote_port" $split_ip {
    33%    192.168.1.10;
    33%    192.168.1.20;
    33%    192.168.1.30;
    *      192.168.1.10;
}

location / {
   proxy_bind $split_ip;
   ...
}
```

* Check it

Just run `tcpdump` and check output traffic to backend`

```
# tcpdump -npi any host 192.168.1.30
```
