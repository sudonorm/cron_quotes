pipeline{
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                bat 'echo "code checked out" '
            }
        }

        stage('Create VirtualEnv') {
            steps {
                bat 'python --version' // Add Python path to system environment variable 
                bat 'python pip install virtualenv'
                bat 'virtualenv venv'
                bat 'echo "set-up done" '
            }
        }

        stage('Get Quotes') {
            steps {
                bat 'pip -V'
            }
        }
    }
 
    //post {
    //    always {
     //           cleanWs()
     //           }
	//}
}