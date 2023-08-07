# Modules 

## Preconditions:

Python includes several preinstalled modules

## How to check available modules without pip, conda and so forth

```bash
$ python
>>> help("modules")
```

Or as oneline

```bash
$ python -c "help('modules')"
```

## Module `http` server. 
Python can run a http server outbox.
> If you want to assign a port from range less 1500 that requires root premissions.

```bash
$ python3 -m http.server 3000
```

## Module `json` improves an output.
Python exists a `json` module. Module parses and showes any valide json in readable format.

```bash
$ curl https://rickandmortyapi.com/api/character/1 -s | python3 -m json.tool
```

