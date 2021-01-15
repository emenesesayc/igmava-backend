pipeline {
    agent { docker { image 'python:3.8.3' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'sudo apt install mysql-server'
                    sh 'mysql -uroot --execute="show databases;"'

		    sh 'export USER=root && unzip ngrok-stable-linux-amd64.zip'
		    sh 'export USER=root && ./ngrok authtoken 1mgbvqQdT8fXNrXKn0QOWiXqm7C_cAdE7VuRewUbtrW8w9nB'
                    sh 'export USER=root && pip install --user -r requirements.txt' //aqui no creo que sea necesario pero por si las moscas
		    sh 'ip address'
		    sh 'export USER=root && export USE_NGROK=True && export FLASK_ENV=development && export FLASK_APP=groktest.py && python -m flask run'
                }
            }
        }
    }
}
