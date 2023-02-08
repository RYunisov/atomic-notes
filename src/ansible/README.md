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

### Escape go template `{{` `}}` symbols

```sh
# Example 01
consul_bind_addr:  "{{ '{{ GetInterfaceIP \\\"eth0\\\" }}' }}"
consul_advertise_addr:  "{{ '{{ GetInterfaceIP \\\"eth1\\\" }}' }}"

# Example 02
UsernameTemplate: "{{ '{{ username }}' }}"
```

### Usefull tips
```bash
--diff - for check differens
--check - just dry-run
```
