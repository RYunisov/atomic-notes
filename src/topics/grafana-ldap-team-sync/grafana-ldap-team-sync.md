# Grafana OSS and LDAP Team sync

That feature available only on Enterprise edition.
However spend some time to investigate opensource repo and the solution was found.

> Note: The patch was tested on 11.5.1 version

[Here](https://github.com/RYunisov/atomic-notes/blob/main/src/topics/grafana-ldap-team-sync/ldap_team_sync.patch) I would like to share git-patch as draft.

# How to implement the git-patch

* Clone original version

```
git clone https://github.com/grafana/grafana.git
```

* Checkout `v11.5.1` version

```
git checkout v11.5.1
```

* Apply git-patch

```
git apply ldap_team_sync.patch
```

* Build docker image

```
make build-docker-full
```

Last step is creating a docker image `grafana/grafana-oss:dev`.

# Run container

* Setup LDAP config to connect into your AD resource

* Provide `config.ini` with defined Team based on LDAP Group

```
[[servers.team_mappings]]
team = "g_o_admin"
group_dn  = "CN=G_O_Admin,OU=Groups,DC=domain,DC=local"
email      = "no_reply@domain.local"
org_id    = 1
[[servers.team_mappings]]
team = "g_o_staff"
group_dn  = "CN=G_O_Staff,OU=Groups,DC=domain,DC=local"
email      = "no_reply@domain.local"
org_id    = 1
```
 
* Login with ldap account which has one of provided group

* Check teams in Grafana UI. The user has to assigned into the group as `Admin`
