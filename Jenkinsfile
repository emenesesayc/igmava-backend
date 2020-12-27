pipeline {
	agent { docker 
	       {image 'python:3.8.3' }
	      }
	stages {
		stage('build') {
			steps {
				sh 'virtualenv venv --distribute'
				sh '. venv/bin/activate'
				sh 'pip install -r requirements.txt'
			}
		}
		stage('deploy') {
			steps {
				sh 'python igmavaAPI.py'
			}
		}
	}
}
