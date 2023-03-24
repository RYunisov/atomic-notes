# Nginx as reserse-proxy for SSH

You need create a `stream` and defined SSL

```bash

stream {

    map $ssl_server_name $target_backend {
        host01 192.168.10.223:22;
        host02 192.168.10.222:22;
        host03 192.168.10.112:22;
    }

    server {

        listen 8443 ssl; # managed by Certbot
        ssl_certificate /etc/letsencrypt/live/gw.digimatics.ru/fullchain.pem; # managed by Certbot
        ssl_certificate_key /etc/letsencrypt/live/gw.digimatics.ru/privkey.pem; # managed by Certbot
        ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

        proxy_pass      $target_backend;

    }

}

```

Command example to run SSH connect will be look like below:
```
ssh -o "ProxyCommand=openssl s_client -quiet -servername %h -connect <IP_LOADBALACE>:8443" host01
```
