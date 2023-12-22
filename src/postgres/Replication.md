# Postgres 13 replication

## Master node

Create role with replication permission

```
CREATE ROLE replica_user WITH REPLICATION LOGIN PASSWORD '<PLAIN_PASSWD>';
```

Update `pg_hba.conf` to make connection between master and replica nodes

```
...
host  replication   replica_user  172.16.10.0/24   md5
...
```

Check backup/steaming

```
SELECT client_addr, state FROM pg_stat_replication;
```

## Replica node

Stop postgresql instance

Remove old data from PG_DATA directory

Run backup

```
pg_basebackup -h 194.195.208.82 -U replica_user -X stream -C -S replica_1 -v -R -W -D $PG_DATA
```

