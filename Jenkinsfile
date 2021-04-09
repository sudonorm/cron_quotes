pipeline{
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                bat 'python --version'
            }
        }

        stage('check Python version') {
            steps {
                bat 'python --version'
            }
        }

        stage('check pip') {
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