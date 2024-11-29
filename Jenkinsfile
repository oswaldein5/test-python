pipeline {
    agent {
        // Definir el agente para ejecutar el pipeline en un nodo con la etiqueta 'docker'
        label 'docker'
    }

    environment {
        // Establecer la variable de entorno para el correo electrónico del destinatario
        RECIPIENT_EMAIL = 'oswaldo.solano172@comunidadunir.net'
    }

    stages {
        stage('Source') {
            steps {
                // Obtener el código fuente del repositorio Git y la rama especificada
                git branch: 'main', url: 'https://github.com/oswaldein5/test-python'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Ejecutar el comando de construcción usando Makefile
                    sh 'make build'
                }
            }
        }

        stage('Unit Tests') {
            steps {
                script {
                    // Ejecutar pruebas unitarias usando Makefile
                    sh 'make test-unit'
                }
            }
            post {
                always {
                    // Archivar los resultados de las pruebas unitarias
                    archiveArtifacts artifacts: 'results/unit_result.xml', allowEmptyArchive: true
                }
            }
        }

        stage('API Tests') {
            steps {
                script {
                    // Ejecutar pruebas de API usando Makefile
                    sh 'make test-api'
                }
            }
            post {
                always {
                    // Archivar los resultados de las pruebas de API
                    archiveArtifacts artifacts: 'results/api_result.xml', allowEmptyArchive: true
                }
            }
        }

        stage('E2E Tests') {
            steps {
                script {
                    // Ejecutar pruebas de extremo a extremo usando Makefile
                    sh 'make test-e2e'
                }
            }
            post {
                always {
                    // Archivar los resultados de las pruebas de extremo a extremo (E2E)
                    archiveArtifacts artifacts: 'results/cypress_result.xml', allowEmptyArchive: true
                }
            }
        }
    }

    post {        
        failure {
            script {
                // Imprimir un mensaje en la consola si el pipeline falla
                echo "Pipeline failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
            }
            // Enviar una notificación por correo electrónico si el pipeline falla
            // emailext (
            //     to: "${env.RECIPIENT_EMAIL}",
            //     subject: "Pipeline failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            //     body: "El pipeline ${env.JOB_NAME} #${env.BUILD_NUMBER} ha fallado. Por favor, revise la salida de la consola de Jenkins para más detalles.",
            //     attachLog: true
            // )
        }
        always {
            // Publicar los resultados de las pruebas en Jenkins
            junit 'results/*_result.xml'

            // Limpiar el espacio de trabajo después de que el pipeline se complete
            cleanWs()
        }
    }
}