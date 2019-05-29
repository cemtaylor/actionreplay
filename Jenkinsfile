pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.7.3-alpine'
                }
            }
            steps {
                sh 'python -m py_compile actionreplay_app/actionreplay.py actionreplay_app/ui/Ui_ActionReplay.py'
            }
        }
        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python3'
                }
            }
            steps {
                sh 'pyinstaller --onefile actionreplay_app/actionreplay.py'
            }
            post {
                success {
                    archiveArtifacts 'dist-linux/actionreplay'
                }
            }
        }
    }
}