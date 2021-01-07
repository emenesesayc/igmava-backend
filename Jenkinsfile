node {
   stage('Get Source') {
      // copy source code from local file system and test
      // for a Dockerfile to build the Docker image
      git ('https://github.com/emenesesayc/igmava-backend.git')
      if (!fileExists("Dockerfile")) {
         error('Dockerfile missing.')
      }
   }
   stage('Build Docker') {
       // build the docker image from the source code using the BUILD_ID parameter in image name
         sh "sudo docker build -t igmava ."
   }
   stage("run docker container"){
        sh "sudo docker run -p 8008:80 --name igmava -d igmava"
    }
}
