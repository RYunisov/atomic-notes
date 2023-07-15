# OpenSSL

## Tips

In case certificate looks like binary.

Try to check it

```bash

$ openssl x509 -inform der -in <path_cert>

```

Mutate DER to PEM

```bash

$ openssl x509 -inform der -in <path_cert> -outform PEM -out <path_cert_pem>

```
