pipeline {
    agent none
    stages {
        stage('build') {
            steps {
<<<<<<< HEAD
                sh 'docker build -t igmava .'
                sh 'docker run -d -p 8008:80 igmava'
=======
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
		    sh 'ls'
		    sh 'python main.py'
                }
>>>>>>> dd7fd0eb74bf789a8efc22f20af2a4aa24c35438
            }
        }
    }
}
