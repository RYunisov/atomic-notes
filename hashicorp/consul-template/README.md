# Consul-template

## Breif

The tool can make an easier process to get data from Hashicorp utils like as Consul, Nomad, Vault.

I think the util easy to configure, not require a lot resouces and can cover a lot case in dynamic infrastructure.

Review the examples: 
* Get service from Consul and prepare vhost configurations for Nginx
* Processing rotation certificates from Vault and updated them into target hosts

## Tips

### Get data from Consul

Prepare config:

```hcl
consul {
    address = "<consul_addr>:<consul_port>"
}
template {
  source      = "./template.d/nginx-vhost.tpl"
  destination = "/etc/nginx/conf.d/nginx-vhosts.conf"
  perms       = 0644
  command     = "nginx -s reload"
}
``` 

Prepare template:

```tpl
{{ range services }} {{$name := .Name}} {{$service := service .Name}} {{$tags := .Tags | join ","}}
{{ if and ($tags | contains "traefik") ($name | contains "sidecar" | not) }}
server {
    listen 80;
    listen [::]:80;
    server_name {{$name}};

    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name {{$name}};

    location / {
{{- range $service }}
        proxy_pass http://{{.Address}}:{{.Port}};
{{- end }}
    }
}
{{ end }}
{{ end }}
```

### Sign cert from pki secret engine in Vault

Prepare config as `cert.hcl`:

```hcl
vault {
  address      = "<vault_addr>:<vault_port>"
  token        = "<vault_token>"
  unwrap_token = false
  renew_token  = true
}
template {
  source      = "/etc/consul-template.d/templates/agent.cert.tpl"
  destination = "/etc/nginx/ssl/certs/client.nomad.key.pem"
  perms       = 0644
  command     = "systemctl reload nomad"
}
template {
  source      = "/etc/consul-template.d/templates/agent.key.tpl"
  destination = "/etc/nginx/ssl/keys/client.nomad.key.pem"
  perms       = 0644
  command     = "systemctl reload nomad"
}
```

Prepare template `agent.cert.tpl`:

```tpl
{{ with secret "<vault_secret_engine_path>/issue/nomad-cluster" 
    "common_name=<COMMON_NAME>"
    "ttl=24h"
    "alt_names=localhost" 
    "ip_sans=127.0.0.1" }}
{{ .Data.certificate }}
{{ end }}
```

Prepare template `agent.key.tpl`:

```tpl
{{ with secret "<vault_secret_engine_path>/issue/nomad-cluster" 
    "common_name=<COMMON_NAME>"
    "ttl=24h"
    "alt_names=localhost"
    "ip_sans=127.0.0.1" }}
{{ .Data.private_key }}
{{ end }}
```

Run consul-template:

```shell
# consul-template -config=./cert.hcl
```
