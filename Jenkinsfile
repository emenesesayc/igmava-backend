pipeline {
        agent { docker {image 'python:3.8.3' } }
        stage('Build') {
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
		    sh 'python igmavaAPI.py'
                }
            }
            post {
                always {
                    echo 'Listoco'
                }
            }
        }
         
    }
}
