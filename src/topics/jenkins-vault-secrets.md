# How to Jenkins retrieve secrets from Hashicorp Vault

Let's see an example to store sensetive data in Hashicorp Vault and retrive these values in Jenkins pipeline;

## Preparation
 * Vault
 * Jenkins
   * Hashicorp Vault plugin: `359.v2da_3b_45f17d5`

## Steps

Create KV secret in Vault.

```bash
$ vault kv put jenkins/foo key=secret
```

Prepare policy. That needs to separate permissions between other authorized users, approles and etc.

```bash
$ cat <<EOF> jenkins-policy.hcl
path "jenkins/data/*" {
  capabilities = ["read"]
}
```

> Note: Path contains `/data/` this isn't mistake, it's important part of path for KV version 2.

Create the policy in Vault.

```bash
$ vault policy write jenkins-policy ./jenkins-policy.hcl
```

Basically vault provides several options to auth. Create a new auth engine as `approle`.

We use the auth engine because it using like as `service_account` and easy to integrate with Jenkins.

```bash
$ vault write auth/approle/role/jenkins \
    secret_id_ttl=0 \
    token_ttl=20m \
    token_max_ttl=30m \
    token_policies="jenkins-policy"
```

Get `role_id` for a created appRole

```bash
$ vault read auth/approle/role/jenkins/role-id

# role_id     db02de05-fa39-4855-059b-67221c5c2f63
```

Get `secret_id` for a created appRole.
> Note: If you already use `secret_id` that cmd will overriding old value.

```bash
$ vault write -f auth/approle/role/jenkins/secret-id

# secret_id               6a174c20-f6de-a53c-74d2-6018fcceff64
# secret_id_accessor      c454f7e5-996e-7230-6074-6ef26b7bcf86
# secret_id_ttl           10m
# secret_id_num_uses      40
```

In case if you would like to check what policies assigned or get `token`.

```bash
$ vault read auth/approle/login \
    role_id=db02de05-fa39-4855-059b-67221c5c2f63 \
    secret_id=6a174c20-f6de-a53c-74d2-6018fcceff64

Key                     Value
---                     -----
token                   s.XXXXX
token_accessor          XXXXX
token_duration          20m
token_renewable         true
token_policies          ["default" "jenkins-policy"]
identity_policies       []
policies                ["default" "jenkins-policy"]
token_meta_role_name    jenkins
```

In Jenkins side requires to create a credential as appRole

Go to:

`Manage Jenkins -> Manage Credentials -> Use global -> Add Credentials -> Vault App Role Credential`

See an example filled fields:

```yaml
Role ID:      db02de05-fa39-4855-059b-67221c5c2f63
Secret ID:    6a174c20-f6de-a53c-74d2-6018fcceff64
Path:         approle
Namespace:
ID:           vault-jenkins-approle
Description:  AppRole for Jenkins
```

Also need setup connect Jenkins and Vault

Go to:

`Manage Jenkins -> Configure System -> Vault Plugin`

```yaml
Vault URL:        https://vault.local
Vault Credential: AppRole for Jenkins
```

This is all for connect Jenkins and Vault. Next steps are describe as get KV secret from Vault

Define an example secret in Jenkins

Go to: 
`Manage Jenkins -> Manage Credentials -> Use global -> Add Credentials -> Vault Secret Text Credential`

See an example filled fields:

```yaml
Namespace:          <STAY EMPTY>
Prefix Path:        <STAY EMPTY>
Path:               jenkins/secret01
Vault Key: key      key
K/V Engine Version: 2
ID:                 vault-secret01
Description:        Vault Example SecretKey
```
> Note: If you click `Test Vault Secrets retrival` Jenkins tries to get value from Vault.

Create a simple job with kind as declarative pipeline

Note: Result might be find in `.secret` file in `Workspace` of job.

```Groovy
pipeline {
    agent any
    environment {
        SECRET = credentials('vault-secret01')
    }
    stages {
        stage("Apply secret") {
            steps {
                sh("echo ${SECRET} > .secret")
            }
        }
    }
}
```

