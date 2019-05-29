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
                sh 'docker run -v "$(pwd):/src/" cdrx/pyinstaller-linux "apt-get update -y && apt-get install -y wget && pip install -r requirements.txt && cd actionreplay_app; pyinstaller --clean -y --dist ../dist/linux --one-dir actionreplay.py'
            }
            post {
                success {
                    archiveArtifacts 'dist-linux/actionreplay'
                }
            }
        }
    }
}