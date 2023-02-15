# Systemd

It is a successor init.

## Tips

* Check status of unit

```bash
$ systemctl status <unti>
```

* List of all units

```bash
$ systemctl list-units
```

* Listing logs by unit

```bash
$ journalctl -f -u <unit>
```

