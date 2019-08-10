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
                    image 'cemt1990/pyinstaller:latest'
                }
            }
            steps {
                sh 'pip install -r requirements.txt && pyinstaller --clean -y --dist ./dist --workpath /tmp --onefile actionreplay.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/actionreplay'
                }
            }
        }
    }
}