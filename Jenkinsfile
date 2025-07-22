pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning the GitHub repository...'
                checkout scm
            }
        }

        stage('Install Requirements') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip3 install --upgrade pip setuptools wheel pytest numpy'
            }
        }

        stage('Build Package') {
            steps {
                echo 'Building the Python package...'
                sh 'python3 setup.py sdist bdist_wheel'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh 'pytest --junitxml=test-results.xml'
            }
        }

        stage('Archive Artifacts') {
            steps {
                echo 'Saving build outputs...'
                archiveArtifacts artifacts: 'dist/*.whl, dist/*.tar.gz, test-results.xml'
            }
        }

    }
}

