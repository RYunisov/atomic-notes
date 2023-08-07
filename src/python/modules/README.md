# Modules 

## Preconditions:

Python includes several preinstalled modules

Http server. Python can run a http server outbox.
> If you want to assign a port from range less 1500 that requires root premissions.

```bash
$ python3 -m http.server 3000
```

Parse json output.
Python exists a `json` module. Module will parse and show in readable format.

```bash
$ curl https://rickandmortyapi.com/api/character/1 -s | python -m json.tool
```

