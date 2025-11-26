pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/TU_USUARIO/ci-demo.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_main.py'
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 main.py'
            }
        }
    }

    post {
        success {
            echo "Pipeline ejecutado con éxito!"
        }
        failure {
            echo "El pipeline falló."
        }
    }
}

