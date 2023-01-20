# Ansible

## Examples:

### Run any shell command on `host_group`
```sh
ansible <host_group> -m shell -a 'uptime' -vv
```