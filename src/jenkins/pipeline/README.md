# Declarative pipeline

## Tips

* Escaping symbols `'` single quote

```groovy
def text = '"\$ENV1, \$ENV2"';

pipeline {
    agent any;
    stages {
        stage("Escaping single quote") {
            steps {
                sh """
                    bash -c ' echo '"'"'${text}'"'"' '
                """
            }
        }
    }
}

// Output
// [Pipeline] sh (hide)
// + bash -c ' echo '\''"$ENV1, $ENV2"'\'' '
// "$ENV1, $ENV2”
```
