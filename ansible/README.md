# Ansible

## Precondition:

Let's say ansible project has similary structure:

```sh
foo_project/
  ansible.cfg
  roles/
    role_01/
      tasks/
        main.yml
      defaults/
        main.yml
  inventories/
    host_vars/
      any_host
    group_vars/
      any_group
    production
```

## Examples:

### Run any shell command on `host_group`

```sh
$ ansible <host_group> -m shell -a 'uptime' -vv
```
