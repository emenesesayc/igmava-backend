pipeline {
    agent { docker { image 'python:3.8.3' } }
	
	

    stages {
	stage('Prepare venv') {
	    steps {
		script {
		    if (isUnix()) {
			env.ISUNIX = "TRUE" // cache isUnix() function to prevent blueocean show too many duplicate step (Checks if running on a Unix-like node) in python function below
			sh 'python3 -m venv pyenv'
			PYTHON_PATH =  sh(script: 'echo ${WORKSPACE}/pyenv/bin/', returnStdout: true).trim()                        
		    }
		    else {
			env.ISUNIX = "FALSE"
			powershell(script:"py -3 -m venv pyenv") // windows not allow call python3.exe with venv. https://github.com/msys2/MINGW-packages/issues/5001
			PYTHON_PATH =  sh(script: 'echo ${WORKSPACE}/pyenv/Scripts/', returnStdout: true).trim()
		    }

		    try  {
			// Sometime agent with older pip version can cause error due to non compatible plugin.
			Python("-m pip install --upgrade pip")
		    } 
		    catch (ignore) { } // update pip always return false when already lastest version
		    // After this you can call Python() anywhere from pipeline
		    Python("-m pip install -r requirements.txt")
		}  
		sh 'python igmavaAPI.py'    
	    }
	}
	stage('Deploy') {
		steps {
		    sh '. pyenv/bin/activate'
		    
		    sh '. pyenv/bin/activate'
		    sh 'FLASK_APP=igmavaAPI.py flask run --host 0.0.0.0 --port 8008'		
		}		
	}
    }
}	    
	    
// Several plugins like WithPyenv is not working perfectly accross platform when using Virtual Env.
// Put this method outside pipeline
def Python(String command) {
    if (env.ISUNIX == "TRUE") {
        sh script:". pyenv/bin/activate && python ${command}", label: "python ${command}"
    }
    else {
        powershell script:"pyenv\\Scripts\\Activate.ps1 ; python ${command}", label: "python ${command}"
    }
}

