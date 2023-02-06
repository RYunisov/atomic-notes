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
