pipeline{
    agent any
    
    triggers {
        cron('H 8 * * *') // Run script everyday at 8:53am 
    }
    stages {
        stage('Checkout Code') {
            steps {
                bat 'echo "code checked out" ' // this stage can be used if "pipeline with SCM" is not selected while setting up the job
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
                    
                    withCredentials([string(credentialsId: 'job-username', variable: 'jobUserName')]) {

                        bat 'echo Started By: %jobUserName%'
                        bat 'venv/Scripts/activate'
                        bat 'python get_quotes.py -u %jobUserName%' // run python script with the username as an input
                        bat 'echo "file run"'

                        }
                }
                
            }
        }
    }
 
    post {
        always {
                cleanWs() // clean up workspace
            }
	    }
}