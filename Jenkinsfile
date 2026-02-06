pipeline {
    agent any

    environment {
        FLASK_ENV = "development"
        FLASK_APP = "app.py"

        DB_HOST = "localhost"
        DB_NAME = "testdb"
        DB_USER = "testuser"
        DB_PASSWORD = "testpass"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                sh '''
                python --version || python3 --version
                '''
            }
        }

        stage('Setup Python Venv') {
            steps {
                sh '''
                python3 -m venv venv || python -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Basic App Test') {
            steps {
                sh '''
                . venv/bin/activate
                python -c "import app; print('App import successful')"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
