# Ansible-playbook

It is collect of task described in playbook

## Tips:

* The most high priority of variable

`-e EXTRA_VARS, --extra-vars EXTRA_VARS`

```bash
$ ansible-playbook -i hosts --extra-vars "variable_var=foo"
```

