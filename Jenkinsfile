pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
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
