# Ldapsearch

## Precondition

* Check util `ldap-utils` installed in Ubuntu distr
* Check certs installed in TLS/SSL case

### Show LDAP information for person object
```sh
$ ldapsearch -H 'ldaps://<ldap_host>:636' \
             -D "<bind_dn>" \
             -w '<bind_dn_password>' \
             -b "<search_dn>" \
             "(&(objectClass=person)(sAMAccountName=<LDAP_USERNAME>))"
```

