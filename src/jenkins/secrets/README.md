# Secret

## Show secrets from Jenkins credential store

* Go to a link `https://<jenkins_link>/manage/script`
* Paste snippet:

```Groovy
com.cloudbees.plugins.credentials.SystemCredentialsProvider.getInstance().getCredentials().forEach{
  it.properties.each { prop, val ->
    if (prop == "secretBytes") {
      println(prop + "=>\n" + new String(com.cloudbees.plugins.credentials.SecretBytes.fromString("${val}").getPlainData()) + "\n")
    } else {
      println(prop + ' = "' + val + '"')
    }
  }
  println("-----------------------")
}
```

## The simple Groovy oneline

```groovy
// Use credentialId which store on Credential Stores
def credId = 'vault-token-name';


// Information regarding methods you can find here: https://javadoc.jenkins.io/hudson/util/Secret.html?is-external=true
def vaultSecret = com.cloudbees.plugins.credentials.SystemCredentialsProvider.getInstance().getStore().getCredentials(
com.cloudbees.plugins.credentials.domains.Domain.global()
).find { it.getId().equals(credId) }.getSecret().getPlainText()

```

