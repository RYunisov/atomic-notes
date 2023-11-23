# Vault

The secret store for credentials

## Tips

How to create the token without TTL. Application or service can be renew a token and continue using it.
> However it can be dangerous because tokens should be rotate every time for the secure reasons.

	vault token create -ttl=0 -period=24h
