pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.8.3' 
                }
            }
            steps {
                sh 'sh 'pip install -r requirements.txt''
            }
        }
    }
}
