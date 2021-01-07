pipeline {
    agent none
    stages {
        stage('build') {
            steps {
                sh 'docker build -t igmava .'
                sh 'docker run -d -p 8008:80 igmava'
        }
    }
}
