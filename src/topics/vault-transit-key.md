# Vault and `transit key`

Description:

Vault can cover a sensitive data by `transit key`. `Transit key` can store outside Vault.

As instance the data covered by transit key on Vault:

```
some_api_token = {
    accessor_id = "vault:v1:N76+aQS2WTEeNHp/W1FF6olPnRFUaYPAFTkzfGOpOzNTl+quqBClVJYNNIEep/tkJ7w7UirbiEv1QDuOSpzuDg=="
    secret_id   = "vault:v1:mDzHh6nIShpva50/fKeJVv8kMk9r3JkJFlHpKouNBDfUiAet8aWRLTpTje/Tkp5GNBe4GjySNq++W1Hq7Wcj6w=="
}
```

As an example the feature can use to cover a sensitive data in Terraform

# How to do use it

## Create secret engine and create key

Make sure kind of secret is enabled:

```
$ vault secret list
Path          Type         Accessor              Description
----          ----         --------              -----------
transit/      transit      transit_cf2e9807      n/a
```

In case if it disabled. Enabled it:

```
$ vault secret enable transit
Success! Enabled the transit secrets engine at: transit/
```

Create an example `transit key`:

```
$ vault write transit/encrypt/my-example-key plaintext=$(echo "my secret data" | base64)
Key           Value
---           -----
ciphertext    vault:v1:8SDd3WHDOjf7mq69CyCqYjVVViQQAVZRkFM13ok481zoCmHnSeDX9vyf7w==
```

## Backup the key:

Check a ciphertext for a key:

```
$ vault read transit/backup/my-example-key
Key       Value
---       -----
backup    XXXXX
```

Store the backup value in the other secret store like as 1Password, LastPass or etc.

## Restore key:

Create the secret engine with type `transit`:

```
$ vault secret enable transit
```

Rollup a backup key:

```
$ export CIPHERTEXT="<text_from_last_pass_in_base64>"
$ vault write transit/restore/my-example-key backup=$CIPHERTEXT
```

Check a restore key:

```
vault read transit/backup/my-example-key
```

