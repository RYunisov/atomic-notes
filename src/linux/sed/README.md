# SED

## Brief

Util for parse text and make change on the fly.

## Tips

### Replace a string on the fly

Let's image the file `service.hcl`:

```hcl
service "%NAME_OF_SERVICE%" {
    name    = "name"
    provide = "consul"
}
```

The goal is change `%NAME_OF_SERVICE%` to other value, as instance `EXAMPLE`:

```bash
sed -i -e 's/%NAME_OF_SERVICE%/EXAMPLE/g'  service.hcl
```

Result:

```hcl
service "EXAMPLE" {
    name    = "name"
    provide = "consul"
}
```
