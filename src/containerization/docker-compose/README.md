# Docker-compose

## Brief

The most easier way to keep config resources for running containers.

Original [`documentation`](https://docs.docker.com/compose/)

## Limitations

* Can not migrate containers between hosts
* Haven't clusters features
* Haven't scale features

## Tips

### Run containers as daemon

```bash
$ docker-compose up -d
```

### Run containers with build

```bash
$ docker-compose up --build -d
```

### Run container as temp
```bash
$ docker-compose run <name_of_service>
```

### Labels

That an important feature. Because can easy to find required container. Also `traefik` can operate with LABELS on docker-compose

```yaml
...
labels:
- stage=production
- version=${GIT_SHA}
- traefik.http.routers.josh-production.rule=Host(`example.com`)
- traefik.http.routers.josh-production.tls=true
...
```

As an example:

```bash
docker ps --filter label=stage=production --format {{.ID}} --all
18672fd97e94
```
