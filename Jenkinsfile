pipeline {
    agent { docker { image 'python:3.8.3' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m pip install --user -r requirements.txt'
                sh 'python src/main.py'
            }
        }
    }
}
