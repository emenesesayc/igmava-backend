pipeline {
    agent { docker { image 'python:3.8.3' } }
    stages {
        stage('build') {
            steps {
                sh 'docker run -dit --name igmava -p 8008:80'
            }
        }
    }
}
