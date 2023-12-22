# Postgres

Relation dababase

## Tips

Just connect to Postgres in localhost

```bash

% psql

```

Make backup a full backup

```bash

% pg_dumpall > full_dump.sql

```

Check tablespaces

```bash

postgres=# \db

```

# Check roles:

```
  SELECT * FROM pg_roles;
```

# Update password on Role:

```
  ALTER ROLE replica_user ENCRYPTED PASSWORD '<PASSWORD>';
```
