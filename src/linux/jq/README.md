# JQ

Easy parse from JSON to output

## Brief

* Written on Python
* Don't faster

## Tips

* Show only `HTTP_CODE` 500 and print as `tab` table
```
tail -f /var/log/nginx/access.log | \
  jq -r '[.time_local,.remote_addr,(.status | select(contains("500"))),.request_time,.upstream_response_time,.request] | @tsv'
```

* Show request contains a pattern
```
tail -f /var/log/nginx/access.log | \
  jq -r 'select(.request | contains("feedback/attach")) | [.time_local,.client_addr,.status,.request_time,.upstream_response_time,.request] | @tsv'
```

* Apply two sequence filters and setup limit to the request field just 80 symbols
```
tail -f /var/log/nginx/access.log | \
  jq -r 'select(.status != "200") | select(.request | contains("/api/health")) | [.time_local,.remote_addr,.status,.request_time,.upstream_response_time,.request[0:80]] | @tsv'
```
