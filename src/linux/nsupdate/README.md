# Nsupdate

Tool `nsupdate` relied to manage DNS records, zones and etc

## Tips

* Add a new record to zone

```bash
$ nsupdate
> server ns1.example.com
> update add record01.example.com. 3600 IN A
> send
```

* Add a new `CNAME` record to zone

```bash
$ nsupdate
> server ns1.example.com
> update add record02.example.com. 3600 CNAME record01.example.com.
> send
```

* Delete a record

```bash
$ nsupdate
> server ns1.example.com
> update delete record01.example.com.
> send
```

