# Top 5 docker commands which rare using.

However they are really helpful in during troubleshouting process.

* How to check mounted volumes into container

Docker `inspect` provide broad information about running container.
As example it can helpful for understand how does a container running.

```bash

# docker inspect <CONTAINER_ID> --format "{{.Mounts}}"

OUTPUT:

[{volume loki_data /var/lib/docker/volumes/loki_data/_data /tmp local rw true }]

```

* Check layouts on images

The command presents all layouts which was used in due build an image

```bash
# docker history <IMAGE_ID>

OUTPUT:

IMAGE          CREATED       CREATED BY                                      SIZE      COMMENT
6a72af05e4cd   3 weeks ago   ENTRYPOINT ["/opt/main"]                        0B        buildkit.dockerfile.v0
<missing>      3 weeks ago   COPY /opt/sources/main /opt/main # buildkit     14.4MB    buildkit.dockerfile.v0
<missing>      3 weeks ago   RUN /bin/sh -c apk add curl # buildkit          6.02MB    buildkit.dockerfile.v0
<missing>      4 weeks ago   /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
<missing>      4 weeks ago   /bin/sh -c #(nop) ADD file:32ff5e7a78b890996…   7.34MB
```

* Use filter and search in a container logs 

That isn't a simple shows logs and also apply filter and search inside.

```bash

# docker logs <CONTAINER_ID> > service.log 2>&1; less service.log

```

* Remove all containers with state is `Exited`

The bash command uses the inhire expansion in the regular docker command as `rm`.

```bash

# docker rm $(docker ps -a --filter state=exited --format "{{.ID}}")

OUTPUT:

eba7c4377515
95453b1629a6
```

* Show statictics on running services on Docker

That command presents main metrics as CPU, RAM and Network are using in current time per container or all containers

```bash

# docker stats

OUTPUT:

CONTAINER ID   NAME                            CPU %     MEM USAGE / LIMIT     MEM %     NET I/O           BLOCK I/O         PIDS
eba7c4377515   container_1                     93.39%    26.83MiB / 15.66GiB   0.17%     1.26TB / 256GB    65.2MB / 180kB    9
95453b1629a6   container_2                     47.55%    36.37MiB / 15.66GiB   0.23%     873GB / 4.12TB    44.7MB / 24.7GB   10
7bb9024de518   container_3                     0.00%     5.922MiB / 15.66GiB   0.04%     10.6MB / 196MB    7.84MB / 0B       5
4c720b536401   container_4                     0.59%     2.164GiB / 15.66GiB   13.81%    133GB / 654GB     16GB / 10.6GB     224

```

