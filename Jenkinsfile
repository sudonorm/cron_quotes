pipeline{
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                bat 'python --version'
            }
        }
    }
    
    post {
        always {
                cleanWs()
                }
	}
}