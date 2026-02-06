pipeline {
    agent any

    environment {
        COMPOSE_PROJECT_NAME = "localtest"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Create Environment File') {
            steps {
                sh '''
                cat <<EOF > .env
POSTGRES_DB=appdb
POSTGRES_USER=appuser
POSTGRES_PASSWORD=apppass

DB_HOST=db
DB_PORT=5432

BACKEND_PORT=8000
FRONTEND_PORT=3000
EOF
                '''
            }
        }

        stage('Clean Previous Run') {
            steps {
                sh '''
                docker-compose down --remove-orphans || true
                '''
            }
        }

        stage('Build Images') {
            steps {
                sh '''
                docker-compose build --no-cache
                '''
            }
        }

        stage('Start Application') {
            steps {
                sh '''
                docker-compose up -d --force-recreate
                '''
            }
        }

        stage('Wait for Services') {
            steps {
                sh '''
                echo "Waiting for backend..."
                for i in {1..15}; do
                  curl -s http://localhost:8000 && break
                  sleep 2
                done

                echo "Waiting for frontend..."
                for i in {1..15}; do
                  curl -s http://localhost:3000 && break
                  sleep 2
                done
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                docker ps

                curl -f http://localhost:8000
                curl -f http://localhost:3000
                '''
            }
        }
    }

    post {
        always {
            sh 'docker-compose ps'
        }

        failure {
            sh 'docker-compose logs'
        }
    }
}

