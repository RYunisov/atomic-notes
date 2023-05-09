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

`/` - The path where find object

`type f` - The type is a file

`type d` - The type is a directory

`name` - The name object for find

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

### Pipe or conveyer

- Pass value as arguments to the pipeline

```bash
# ls /home/*/.ssh/authorized_keys | xargs -I {} bash -c "echo -n {}; cat {}"
```

- Check counts to target IP

```bash

ss -tan | grep EST | grep <IP_DEST> | awk '{ print $4 }' | tr ":" " " | awk '{ print $1 }' | sort | uniq -c

```

### bashrc

- Connect to host with specific port and separate ":" by ssh

Update bashrc or zshrc file

```
# ssh 127.0.0.1:2888

function ssh() {
  if [[ "${1}" == *":"* ]]; then
    ARG_HOST=$(echo "${1}" | cut -d : -f 1)
    ARG_PORT=$(echo "${1}" | cut -d : -f 2)
    /usr/bin/ssh ${ARG_HOST} -p ${ARG_PORT} ${@:2}
  else
    /usr/bin/ssh $@
  fi
}
```
