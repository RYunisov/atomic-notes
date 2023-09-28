# WGet

Basically `curl` can replace that tool. However sometime will be useful know some tricks.
Compare with `curl`, `wget` can download recursive and support only HTTP, HTTPs protocols.

* Get only responce without garbage info

```bash
$ wget -qO- https://rickandmortyapi.com/api/character/1
```

* Get HTTP header as responce

```bash
$ wget -S -q https://rickandmortyapi.com/api/character/1
```

