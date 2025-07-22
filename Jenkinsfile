pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install build pytest pytest-xml
                '''
            }
        }

        stage('Build Package') {
            steps {
                sh 'python3 -m build'
            }
        }

        stage('Test Package') {
            steps {
                sh 'pytest tests/ --junitxml=results.xml'
                junit 'results.xml'
            }
        }

    }

    post {
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed. Please check logs.'
        }
    }
}


