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
                    pip install build pytest pytest-cov
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
                sh '''
		   pytest --cov-report html:cov.html tests/ 
		'''
            }
        }
	    
	stage('Archive Artifacts') {
            steps {
		   archiveArtifacts artifacts: 'dist/*.whl'
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

	

