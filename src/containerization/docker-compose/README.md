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

