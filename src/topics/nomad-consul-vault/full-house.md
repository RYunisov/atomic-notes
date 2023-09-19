# The security in Nomad Cluster

Hello everyone,

> Note: I will skipped a process installation Nomad, Consul, Traefik and Vault instances. It will take a focus on details to setup configurations and  the definitions of jobs.

_Description_: The main mission of the topic to provide the full picture how we can defend and improve the security in the Nomad cluster.

Also it will be cover mTLS connectivity between all services in Nomad cluster.

Just one port is open to reach the cluster. As example 8443;

## Scheme:

![scheme.drawio.md](./scheme.drawio.png)

## Requirements:

### Nomad
The orchestrator under QEMU, containers, JAVA and etc instances...

** It depends what do you want the kind of a driver on job would run: QEMU or Docker

### Consul

The feature as Service Mesh and Service Discover requires for store services in catalog

** Optional: Can running as Service task into Nomad Cluster

### Vault

Security storage for storing sensetive data.

** Optional: Can running as Service task into Nomad Cluster

### Traefik v3.0

Just load-balancer with much useful features

** Note: Only v3.0 supports TCPTransport

** Optional: Also can running into Nomad


## Configurations: 

### Nomad:

On server side:

Make sure nomad server nodes have been defined `vault` stanza
```
vault {
  enabled          = true
  address          = "<VAULT_ADDR>"
  token            = "<VAULT_TOKEN>"
  create_from_role = "nomad-cluster"
}
```
On client side:

Client nodes also have to defined `vault` stanza, but without `vault_token`.

Also these nodes have to had `consul` stanza. The address `127.0.0.1:8500` because as I mentioned before consul will running inside Nomad cluster.
```
vault {
  enabled          =  true
  address          = "<VAULT_ADDR>"
}

consul {
  address             = "127.0.0.1:8500"
  grpc_address        = "127.0.0.1:8502"
  client_service_name = "nomad-client" # It is just the name of service on Consul
  auto_advertise      = true
  client_auto_join    = true
}
```

### Consul:

The most important here is `connect` stanza. The responsible for the connection to Vault.

> PKI Certificates required for create temp cert and manage mTLS termination between services.

```
connect {
    enabled = true
    ca_provider = "vault"
    ca_config {
        address = "<VAULT_ADDR>"
        token = "<VAULT_TOKEN>"
        root_pki_path = "consul1/connect_root"
        intermediate_pki_path = "consul1/connect_intermediate"
    }
}
```

### Vault:

Make sure Vault cluster exists all policies and provided tokens are valid.

Policies:

> Note: Similar examples you can find on the official documentation site.

* Nomad cluster policy. Provided VAULT_TOKEN or APP_ROLE have to assign to the policy.
```
# Allow creating tokens under "nomad-cluster" role. The role name should be
# updated if "nomad-cluster" is not used.
path "auth/token/create/nomad-cluster" {
  capabilities = ["update"]
}

# Allow looking up "nomad-cluster" role. The role name should be updated if
# "nomad-cluster" is not used.
path "auth/token/roles/nomad-cluster" {
  capabilities = ["read"]
}

# Allow looking up the token passed to Nomad to validate the token has the
# proper capabilities. This is provided by the "default" policy.
path "auth/token/lookup-self" {
  capabilities = ["read"]
}

# Allow looking up incoming tokens to validate they have permissions to access
# the tokens they are requesting. This is only required if
# `allow_unauthenticated` is set to false.
path "auth/token/lookup" {
  capabilities = ["update"]
}

# Allow revoking tokens that should no longer exist. This allows revoking
# tokens for dead tasks.
path "auth/token/revoke-accessor" {
  capabilities = ["update"]
}

# Allow checking the capabilities of our own token. This is used to validate the
# token upon startup.
path "sys/capabilities-self" {
  capabilities = ["update"]
}

# Allow our own token to be renewed.
path "auth/token/renew-self" {
  capabilities = ["update"]
}
```

* Consul policy:

```
path "/sys/mounts" {
  capabilities = [ "read" ]
}

path "/sys/mounts/consul1/connect_root" {
  capabilities = [ "read" ]
}

path "/sys/mounts/consul1/connect_intermediate" {
  capabilities = [ "read" ]
}

# Needed for Consul 1.11+
path "/sys/mounts/consul1/connect_intermediate/tune" {
  capabilities = [ "update" ]
}

path "/consul1/connect_root/" {
  capabilities = [ "read" ]
}

path "/consul1/connect_root/root/sign-intermediate" {
  capabilities = [ "update" ]
}

path "/consul1/connect_intermediate/*" {
  capabilities = [ "create", "read", "update", "delete", "list" ]
}

path "auth/token/renew-self" {
    capabilities = [ "update" ]
}

path "auth/token/lookup-self" {
    capabilities = [ "read" ]
}
```

### Traefik:

Make sure `traefik` configuration exists below options:

```
[providers.consulCatalog]
  prefix           = "traefik"
  serviceName      = "traefik"
  connectAware     = true
  connectByDefault = false
  exposedByDefault = false

  [providers.consulCatalog.endpoint]
    address = "127.0.0.1:8500" # Use VALUE from nomad variables
    datacenter = "<CONSUL_NAME_DC>"
    scheme  = "http"
```

## The definition of jobs:

All jobs defined on HCL format and might be running on Nomad cluster.

\* Trying to describe all important things mentioned at the HCL file

> Be careful the `<VARIABLES>` should be replaced

### Consul job definition:

```
job "consul-all-in-one" {
  datacenters = ["dc1"]
  namespace = "experimental"
  type = "system"

  group "consul-agent" {

    network {
      mode = "host"

      port "consul_server"   {
        static = "8300"
      }
      port "consul_serf_lan" {
        static = "8301"
      }
      port "consul_serf_wan" {
        static = "8302"
      }
      port "consul_rpc"      {
        static = "8400"
      }
      port "consul_http"     {
        static = "8500"
      }
      port "consul_grpc"     {
        static = "8502"
      }
      port "consul_dns"      {
        static = "8600"
      }
    }

    task "consul-server" {
      driver = "docker"

      template {
          destination = "./config/conf.d/config.hcl"
          left_delimiter = "[["
          right_delimiter = "]]"
          data = <<EOH
log_level = "DEBUG"
datacenter = "consul1"
server = true
bootstrap_expect = 3
retry_join = [
    "<NOMAD_CLIENT_#1>",
    "<NOMAD_CLIENT_#2>",
    "<NOMAD_CLIENT_#3>",
]
recursors = [
    "8.8.8.8",
    "8.8.4.4"
]
client_addr = "0.0.0.0"
bind_addr      = "{{ GetInterfaceIP \"en0\" }}"
advertise_addr = "{{ GetInterfaceIP \"en0\" }}"

connect {
    enabled = true
    ca_provider = "vault"
    ca_config {
        address = "<VAULT_ADDR>"
        token = "<VAULT_TOKEN>"
        root_pki_path = "consul1/connect_root"
        intermediate_pki_path = "consul1/connect_intermediate"
    }
}
addresses {
    http = "0.0.0.0"
}
ports {
    grpc = 8502
}
ui_config {
    enabled = true
}
auto_encrypt {
    allow_tls = false
}
acl {
    enabled = true
    default_policy = "allow"
}
EOH
      }

      config {
        image = "hashicorp/consul:1.13.0"
        command = "agent"
        volumes = [
            "./config/conf.d/config.hcl:/consul/config/config.hcl",
            "./config/tls/agent.pem:/consul/config/tls/agent.pem",
            "./config/tls/agent.key:/consul/config/tls/agent.key",
            "./config/tls/ca.pem:/consul/config/tls/ca.pem",
        ]
        network_mode = "host"
        ports = [
            "consul_server",
            "consul_serf_lan",
            "consul_serf_wan",
            "consul_rpc",
            "consul_http",
            "consul_dns",
            "consul_grpc"
        ]
        mount {
          type = "volume"
          target = "/consul/data"
          source = "consul-data"
          readonly = false
        }
      }
      service {
        name = "consul"
        provider = "nomad"
      }
      resources {
        cpu    = 500 # Mhz
        memory = 256 # MB
      }
    }
  }
}

```

### Traefik job definition

```
variable "image_version" {
  type = string
  default = "traefik:v3.0"
}

variable "namespace" {
  type = string
  default = "experimental"
}

job "traefik" {
  datacenters = ["dc1"]
  namespace   = "${var.namespace}" # change to admin ns

  constraint {
    attribute = "${attr.unique.hostname}"
    operator  = "set_contains_any"
    value     = "<SPECIFIC_NOMAD_CLIENT>"
  }

  group "traefik" {

    network {
      mode = "bridge"

      port "api" {
        static = 8081
      }
      port "http" {
        static = 8080
      }
      port "https" {
        static = 8443 
      }
    }

    service {
      name = "ingress-https"
      port = "https"
      connect {
        native = true
      }
    }

    task "traefik" {
      driver = "docker"

      config {
        image = "${var.image_version}"
        force_pull = true
        volumes = [
          "local/traefik.toml:/etc/traefik/traefik.toml",
          "local/ssl:/etc/traefik/ssl",
        ]
      }

      template {
        data = <<EOF
-----BEGIN CERTIFICATE-----
HERE CAN BE YOUR CERT or `Traefik` CAN CARE ABOUT IT.
-----END CERTIFICATE-----
EOF
        destination = "local/ssl/proxy01.cert"
      }

      template {
        data = <<EOF
-----BEGIN PRIVATE KEY-----
HERE CAN BE YOUR PK or `Traefik` CAN CARE ABOUT IT.
-----END PRIVATE KEY-----
EOF
        destination = "local/ssl/proxy01.key"
      }

      template {
        data = <<EOF
[global]
  checkNewVersion = false
  sendAnonymousUsage = false

[log]
  level = "DEBUG"
   
[entryPoints]
  [entryPoints.http]
    address = ":8080"
  [entryPoints.https]
    address = ":8443"
  [entryPoints.traefik]
    address = ":8081"

[api]
  dashboard = true
  insecure  = true
  debug     = true

[providers.consulCatalog]
  prefix           = "traefik"
  serviceName      = "traefik"
  connectAware     = true
  connectByDefault = false
  exposedByDefault = false

  [providers.consulCatalog.endpoint]
    address = "<NOMAD_CLIENT_IP:NOMAD_CLIENT_PORT>" # Use VALUE from nomad variables
    datacenter = "cluster1"
    scheme  = "http"

[serversTransport]
  insecureSkipVerify = true

[tcpServersTransport]
  insecureSkipVerify = true

[providers.file]
  directory = "/etc/traefik"
  watch = true

[tls]
  [[tls.certificates]]
    certFile = "/etc/traefik/ssl/proxy01.cert"
    keyFile = "/etc/traefik/ssl/proxy01.key"
  [tls.stores]
    [tls.stores.default]
      [tls.stores.default.defaultCertificate]
        certFile = "/etc/traefik/ssl/proxy01.cert"
        keyFile  = "/etc/traefik/ssl/proxy01.key"
EOF

        destination = "local/traefik.toml"
      }
      resources {
        cpu    = 100
        memory = 128
      }
    }
  }
}

```

### The simple QEMU instance with SSH

```
job "simple01" {
  datacenters = ["dc1"]
  namespace   = "experimental"

  meta {
    qcow_name = "simple01.qcow2"
    srv_ssh_port = 25001
    srv_rdp_port = 25002
  }

  group "qemu" {
    network {
      mode = "bridge"
    }

    service {
      name = "${NOMAD_JOB_NAME}"
      port = "${NOMAD_META_srv_ssh_port}" 
      tags = [
        "traefik.enable=true",
        "traefik.consulcatalog.connect=true",
        "traefik.tcp.routers.${NOMAD_JOB_NAME}.entrypoints=https",
        "traefik.tcp.routers.${NOMAD_JOB_NAME}.tls=true",
        "traefik.tcp.routers.${NOMAD_JOB_NAME}.rule=HostSNI(`${NOMAD_JOB_NAME}.domain.com`)",
        "traefik.tcp.routers.${NOMAD_JOB_NAME}.service=${NOMAD_JOB_NAME}",
      ]
      connect {
        sidecar_service {}
      }
    }

    task "run-compute-instance" {
      driver = "qemu"

      artifact {
        source = "https://artifactory.com/artifactory/images/${NOMAD_META_qcow_name}"
        destination = "packer-focal2004"
      }

      resources {
        cpu = 2000
        memory = 4096
      }

      config {
        image_path = "packer-focal2004/${NOMAD_META_qcow_name}"
        accelerator = "kvm"
        args = [
          "-vnc", "none,ipv4",
          "-device", "virtio-net,netdev=user.0",
          "-netdev", "user,id=user.0,hostfwd=tcp::${NOMAD_META_srv_ssh_port}-:22,hostfwd=tcp::${NOMAD_META_srv_rdp_port}-:8443"
        ]
      }
    }
  }
}
```

## How it works:

### Nomad:

* The job has a definition `connect` and `sidecar_service` stanzes; Nomad will pass request of create service to Consul. Then that will creating a service by name option in `service` stanza;
* The `tags` stanza. Traefik will be relying on these tags and register routers and services;
* The `sidecar_service` works only with `Consul Service Discovery`, `Nomad Service Discover` doesn’t support it. 
The stanza means Nomad will be running `exvoy-proxy` task, a together with general task, which can manage a network traffic;
* Do not need run Nomad job with predefined ports; Consul will be know that service using envoy-proxy.

### Consul:

* It requires just one think, but it is really important. It is manage certificates. By that action configuration defined connect stanza and Vault instance;
* `Vault` secret paths as `consul1/connect_intermediate` and `consul1/connect_root` created by Consul automatic. It requires a specific `Vault` policy; 
* These secret paths can safety removed and Consul will be recreate them in during restart;

![consul.png](./consul.png)

### Traefik:

* Should be listen at least two ports. HTTP and TCP traffic; If need UI also API should be opened;
* Because traefik is a LB and make terminate TLS sessions, we need keep root domain certs or use letsencrypt;
* Certificates defined in a config file. Traefik should use a config file as a provider.
* Other provider is Consul instance, it also have to defined in config file; Usually traefik re-read service discovery each few seconds and rely on tags;

```
tags = [
    "traefik.enable=true",
    "traefik.consulcatalog.connect=true",
    "traefik.tcp.routers.${NOMAD_JOB_NAME}.entrypoints=https",
    "traefik.tcp.routers.${NOMAD_JOB_NAME}.tls=true",
    "traefik.tcp.routers.${NOMAD_JOB_NAME}.rule=HostSNI(`${NOMAD_JOB_NAME}.domain.com`)",
    "traefik.tcp.routers.${NOMAD_JOB_NAME}.service=${NOMAD_JOB_NAME}"
]
```

### The final step:

After update list of services, traefik will be registering routers and services on own side;
![traefik.png](./traefik.png)

The example, user can join to target host through HTTPS to QEMU host by SSH

After success configuration and have been deployed all services and jobs.
You can run command:

```
$ ssh -o "ProxyCommand=openssl s_client -quiet -servername %h -connect <loadbalancer_host>:<loadbalancer_port>" <target_hostname>
```
