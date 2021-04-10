pipeline{
    agent any
    options([pipelineTriggers([cron('0 9 * * *')]) ]) // Run script everyday at 9am 

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

                        bat "echo Started By: '${jobUserName}'"

                        bat 'venv/Scripts/activate'
                        
                        bat "python get_quotes.py -u ${jobUserName}"
                        bat 'echo "file run"'

                        }
                }
                
            }
        }
    }
 
    post {
        always {
                cleanWs()
            }
	    }
}