pipeline {
    agent any

    environment {
        EC2_USER = "ubuntu"                     // SSH user for EC2
        EC2_HOST = "3.135.193.246"              // EC2 public IP
        EC2_KEY = credentials('ec2-ssh-private-key')  // Jenkins SSH key credential
        PROJECT_DIR = "/home/ubuntu/DjangoAssignment" // Django project path
    }

    stages {
        stage('Update Code on EC2') {
            steps {
                script {
                    sshagent (credentials: ['ec2-ssh-private-key']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} '
                            # Fail immediately if any command fails
                            set -e

                            # Navigate to project directory (exit if missing)
                            cd ${PROJECT_DIR} || { echo "Error: ${PROJECT_DIR} not found"; exit 1; }

                            # Update code from Git
                            git pull origin main

                            # Create/update virtual environment
                            if [ ! -d "comp314" ]; then
                                python3 -m venv comp314
                            fi

                            # Activate venv and install dependencies
                            source comp314/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt

                            # Django commands
                            python manage.py migrate
                            python manage.py collectstatic --noinput
                            deactivate

                            # Restart Gunicorn (ensure passwordless sudo is set up)
                            sudo systemctl restart gunicorn
                        '
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Code updated and app restarted successfully on EC2!"
        }
        failure {
            echo "Deployment failed. Check Jenkins logs for errors."
        }
    }
}
