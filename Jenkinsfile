pipeline {
    agent {
        label 'docker'
    }

    environment {
        RECIPIENT_EMAIL = 'oswaldo.solano172@comunidadunir.net'
    }

    stages {
        stage('Source') {
            steps {
                git branch: 'main', url: 'https://github.com/oswaldein5/test-python'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'make build'
                }
            }
        }

        stage('Unit Tests') {
            steps {
                script {
                    sh 'make test-unit'
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'results/unit_result.xml', allowEmptyArchive: true
                    junit 'results/unit_result.xml'
                }
            }
        }

        stage('API Tests') {
            steps {
                script {
                    sh 'make test-api'
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'results/api_result.xml', allowEmptyArchive: true
                    junit 'results/api_result.xml'
                }
            }
        }

        stage('E2E Tests') {
            steps {
                script {
                    sh 'make test-e2e'
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'results/cypress_result.xml', allowEmptyArchive: true
                    junit 'results/cypress_result.xml'
                }
            }
        }
    }

    post {
        failure {
            script {
                echo "Pipeline failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
            }
            // emailext (
            //     to: "${env.RECIPIENT_EMAIL}",
            //     subject: "Pipeline failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            //     body: "The pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER} has failed. Please check the Jenkins console output for more details.",
            //     attachLog: true
            // )
        }
        always {
            cleanWs()
        }
    }
}