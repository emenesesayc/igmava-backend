pipeline {
    agent any
    stages {
        stage('build') {
            agent { label 'master' }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'docker stop igmavadb || true && docker rm igmavadb || true'
                    sh 'docker run --name igmavadb -p8010:5432 --env="MYSQL_ROOT_PASSWORD=123" -d mysql/mysql-server:latest'

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
