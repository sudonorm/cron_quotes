pipeline{
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                bat 'python --version'
            }

            steps {
                bat 'pip -V'
            }
        }
    }

    post {
        always {
                cleanWs()
                }
	}
}