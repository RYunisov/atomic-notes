# Configure Opsgenie plugin

Example code

```groovy
import jenkins.*

def opsgenieParams = [
	  apiUrl: "https://api.us.opsgenie.com",
  	apiKey: "credId",
  	tags: "jenkins-stage",
  	teams: "DevOps",
]

Jenkins jenkins = Jenkins.getInstance()

def opsgenie = jenkins.getExtensionList(com.opsgenie.integration.jenkins.OpsGenieNotifier.DescriptorImpl.class)[0]
def formData = [getParameter: {name -> opsgenieParams[name]}] as net.sf.json.JSONObject
def org.kohsuke.stapler.StaplerRequest request

opsgenie.configure(request, formData.getParameter['opsgenieParams'])
opsgenie.save()
jenkins.save()
```
