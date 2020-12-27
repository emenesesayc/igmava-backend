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
                }
            }
            post {
                always {
                    echo 'Librerias Instaladas'
                }
            }
        }
        
        stage('deploy') {
			steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
				    sh 'python igmavaAPI.py'
                }
   
			}
		}
        
        
    }
}
