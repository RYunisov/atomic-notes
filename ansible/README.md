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

### Encrypt string by `ansible-vault`

```sh
$ ansible-vault encrypt_string --name secret_name some_secret
```

### Decrypt encrypted vars by ansible-vault
```sh
$ ansible-vault decrypt <file_encrypted_by_vault>
```
