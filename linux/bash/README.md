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

### Move job in the background

```bash
$ sleep infinity &
```

### Show jobs in background

```bash
$ jobs
```

### Join to background

```bash
$ fg 1
```

### Strong recommend to use aliases

Aliases are extended function in bash and that can reduce your operations.

```bash
$ alias tailf='tail -f'
$ alias ll='ls -la'
```

### Kill process

In case terminate a process

Common using signals:

     1       HUP (hang up)
     2       INT (interrupt)
     3       QUIT (quit)
     6       ABRT (abort)
     9       KILL (non-catchable, non-ignorable kill)
     14      ALRM (alarm clock)
     15      TERM (software termination signal)

```bash
$ kill -<signal_id> <pid>
```

