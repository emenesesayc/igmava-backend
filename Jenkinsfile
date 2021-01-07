pipeline {
    agent { docker { image 'python:3.8.3' } }
    stages {
        stage('build') {
            steps {
                sh 'docker build -t igmava .'
                sh 'docker run -d -p 8008:80 igmava'
            }
        }
    }
}
