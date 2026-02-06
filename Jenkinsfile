pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Start Application') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Verify') {
            steps {
                sh '''
                  docker ps
                  curl -f http://localhost:8000 || true
                  curl -f http://localhost:3000 || true
                '''
            }
        }
    }

    post {
        failure {
            sh 'docker-compose logs'
        }
    }
}

