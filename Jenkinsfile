pipeline {
    agent any

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

