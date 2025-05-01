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
                            echo "Starting deployment..."

                            # Navigate to project directory
                            echo "Changing to project directory..."
                            cd ${PROJECT_DIR} || { 
                                echo "FATAL: Directory ${PROJECT_DIR} not found on EC2";
                                exit 1;
                            }

                            # Force sync with GitHub
                            echo "Syncing with GitHub repository..."
                            git fetch origin
                            git reset --hard origin/main

                            # Clean Python cache
                            echo "Cleaning Python cache..."
                            find . -type d -name "__pycache__" -exec rm -r {} + || true

                            # Virtual environment setup
                            echo "Setting up virtual environment..."
                            if [ ! -d "comp314" ]; then
                                python3 -m venv comp314
                            fi

                            # Install dependencies
                            echo "Installing Python dependencies..."
                            source comp314/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt

                            # Django commands
                            echo "Running Django migrations..."
                            python manage.py migrate
                            echo "Collecting static files..."
                            python manage.py collectstatic --noinput
                            deactivate

                            # Restart Gunicorn
                            echo "Restarting Gunicorn..."
                            sudo systemctl restart gunicorn
                            echo "Verifying Gunicorn status..."
                            sudo systemctl status gunicorn --no-pager
                            echo "Deployment completed successfully!"
                        '
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Code updated and app restarted successfully on EC2!"
        }
        failure {
            echo "❌ Deployment failed. Check Jenkins logs for errors."
            slackSend color: 'danger', message: "Deployment failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
    }
}
