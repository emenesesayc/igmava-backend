pipeline {
    agent { docker { image 'python:3.8.3' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
		    sh 'unzip ngrok-stable-linux-amd64.zip'
		    sh './ngrok authtoken 1mgbvqQdT8fXNrXKn0QOWiXqm7C_cAdE7VuRewUbtrW8w9nB'
                    sh 'pip install --user -r requirements.txt'
		    sh 'ip address'
		    sh 'export USE_NGROK=True && export FLASK_ENV=development && export FLASK_APP=groktest.py && python -m flask run'
		    sh 'export FLASK_APP=igmavaAPI.py && python -m flask run --host 0.0.0.0 --port 8008'//forma alterna tampoco funca
                }
            }
        }
    }
}
