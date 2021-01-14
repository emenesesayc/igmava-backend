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
          stage('Archive') {
            steps {
              archiveArtifacts 'build/**'
            }
          }
        }
    }
    stage('Deploy') {
      agent {
        label 'master'
      }
      options {
        skipDefaultCheckout()
      }
      steps {
        sh 'rm -rf /var/www/igmava'
        sh 'mkdir /var/www/igmava'
        sh 'cp -Rp build/** /var/www/igmava'
        sh 'docker stop igmava || true && docker rm igmava || true'
        sh 'docker run -dit --name igmava -p 8001:80 -v /var/www/igmava/:/usr/local/apache2/htdocs/ httpd:2.4'
      }
    }
  }
}
