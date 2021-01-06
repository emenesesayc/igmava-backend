pipeline {
    agent { docker { image 'python:3.8.3' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
		    sh 'pip install --user -r requirements.txt'
		    sh 'export USER=root && unzip ngrok-stable-linux-amd64.zip'
		    sh 'export USER=root && ./ngrok authtoken 1mgbvqQdT8fXNrXKn0QOWiXqm7C_cAdE7VuRewUbtrW8w9nB'
                    sh 'export USER=root && ngrok http localhost:5000'
		    sh 'export FLASK_APP=igmavaAPI.py && python -m flask run --host 0.0.0.0 --port 8008'//forma alterna tampoco funca
                }
            }
        }
    }
}
