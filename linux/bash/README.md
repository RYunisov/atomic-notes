# Bash

## Brief

`ulimit`, `bg` and etc aren't utils they are commands from bash :smile:

Just type `man bash` to check others.

## Precondition
TBD

### Fill multilines data into a file without an editor

```bash
$ cat <<EOF> <path_to_file>
one line
second line
third line
EOF
```

### The simple circle

```bash
$ for FILE in *; do echo ${FILE} - Foo; done
```

### Find file in filesystem

`/`      - The path where find object 

`type f` - The type is a file

`type d` - The type is a directory

`name`   - The name object for find

`-print` - Additional action, like example is print

```bash
$ find / -type f -name "README.*" -print
```
