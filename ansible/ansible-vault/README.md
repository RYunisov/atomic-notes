# Ansible-vault

## Brief

Ansible-vault is util to encrypt/decrypt sensetive date.

## Tips

### Encrypt a single string 

```sh
$ ansible-vault encrypt_string --name secret_name some_secret
```

### Decrypt encrypted data
```sh
$ ansible-vault decrypt <file_encrypted_by_vault>
```
