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
                bat 'pip install virtualenv'
                bat 'virtualenv venv'
                bat 'echo "set-up done" '
            }
        }

        stage('Get Quotes') {
            steps {
                script {
                    wrap([$class: 'BuildUser']) {
                        def jobUserName = "${BUILD_USER}"
                        }
                }
                bat 'echo Started By: "${BUILD_USER}"'

                bat 'venv/Scripts/activate'
                //bat 'activate'
                //bat 'cd ..'
                //bat 'cd ..'
                bat 'python get_quotes.py'
                bat 'echo "file run" '
            }
        }
    }
 
    //post {
    //    always {
     //           cleanWs()
     //           }
	//}
}