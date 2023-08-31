# Why we have to use Packer as docker-image builder?

Advantages:
* That has several plugins to build images as Docker, QEMU and etc
* It has a native support Vault. Constructions aren't necessary which have had contained consul-template or Vault agent in during build image
* Don’t require to know Dockerfile syntax
* Support several provision like as shell, ansible
* Packer hasn’t layouts
* Also support several stages of building

Disadvantages:
* Packer hasn’t layouts. You can't use a native feature docker as cache. If image is too big, it take a long time for update, push and pull
* Can’t setup a default user
* That requires a little bit an experience in json, hcl format
* `Metadata` is only one option provide access to pure Dockerfile commands

## The instance of a docker-image building

```
packer {
  required_plugins {
    docker = {
      version = ">=0.0.7"
      source  = "github.com/hashicorp/docker"
    }
  }
}

variable "docker_image" {
  type    = string
  default = "debian:stable-slim"
}

variable "docker_tag" {
  type    = string
  default = "master"
}

local "docker_login" {
  expression = vault("secrets/data/jenkins/user", "username")
  sensitive  = true
}

local "docker_password" {
  expression = vault("secrets/data/jenkins/pass", "password")
  sensitive  = true
}

source "docker" "debian" {
  image  = var.docker_image
  commit = true
}

build {
  name = "nomad-client"

  sources = [
    "source.docker.debian"
  ]

  provisioner "shell" {
    inline = [
      "apt update && apt install -y curl unzip",
      "curl -O https://releases.hashicorp.com/nomad/1.3.4/nomad_1.3.4_linux_amd64.zip",
      "unzip nomad_1.3.4_linux_amd64.zip -d /usr/sbin && rm -rf nomad_1.3.4_linux_amd64.zip",
      "apt-get clean autoclean",
      "apt-get autoremove --yes",
      "rm -rf /var/lib/{apt,dpkg,cache,log}"
    ]
  }

  post-processors {

    post-processor "docker-tag" {
      repository = "docker-test.example.com/nomad"
      tags       = [
        "latest",
        "${var.docker_tag}"
      ]
    }

    post-processor "docker-push" {
      login          = true
      login_username = local.docker_login
      login_password = local.docker_password
      login_server   = "docker-test.example.com"
    }

  }
}
```

