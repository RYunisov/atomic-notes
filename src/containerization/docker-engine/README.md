# Docker Engine

## Brief

Docker engine is containerization technology.

Uses: 
* `namespaces`
* `cgroups`

More information in [`Official documentation`](https://docs.docker.com/engine/install/)

## Tips

### Clean apt cache in due build process

```Dockerfile
FROM ubuntu:latest

RUN apt update \
    && apt install -y curl unzip \
    && rm -rf /var/lib/apt/lists/* \
    && apt clean
```

### How to pass secret in build process

> :bulb: That secrets will not be store in an image. Secret will not available after build process.

* Make sure env `DOCKER_BUILDKIT` defined.
* Secret available in the mounted step others steps cannot reach secret.

```bash
$ export DOCKER_BUILDKIT=1
$ docker build --secret  id=secretfile,src=<secret_path> .
```

Other way running as:

```bash
$ DOCKER_BUILDKIT=1 docker build --secret  id=secretfile,src=<secret_path> .
```

Example `Dockerfile`:

```Dockerfile
FROM ubuntu:latest

RUN --mount=type=secret,id=secretfile,dst=/<home_dir>/.ssh/id_rsa \
    git clone git://<target_repo_with_ssh>/<name_of_repo>.git
```

### Save stdout log from container

```sh
$ docker logs <container_name> > <filename_log> 2>&1
```

### Check history of image

```sh
$ docker history <image_id>
```

### Copy all data from container

```sh
$ docker export <container_id> > <name_of_tar>
```
