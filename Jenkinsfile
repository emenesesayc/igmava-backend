pipeline {
  agent none 
  stages {
    stage('Checkout, Test & Build') {
        agent {
          docker {
            image 'wesbarnett/apache-flask:bionic-x86_64'
          }
        }
        environment {
          HOME = '.'
        }
        stages {
          stage('Install') {
            steps {
              sh 'pip install --user -r requirements.txt'
            }
          }
        }
    }
    stage('Deploy') {
      agent {
        label 'master'
      }
      steps {
        sh 'docker stop igmava || true && docker rm igmava || true'
        sh 'docker run -dit --name igmava -p 8008:80 -v /var/www/igmava/:/usr/local/apache2/htdocs/ httpd:2.4'
      }
    }
  }
}
