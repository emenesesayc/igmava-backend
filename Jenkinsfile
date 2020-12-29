pipeline {
    agent { docker { image 'python:3.8.3' } }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
		    
                }
		sh 'FLASK_APP=igmavaAPI.py flask run --host 0.0.0.0 --port 8008'
            }
        }
    }
}
