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
                    // Use SSH to run commands on the EC2 instance
                    sshagent (credentials: ['ec2-ssh-private-key']) {
                        sh """
                        ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} '
                            cd ${PROJECT_DIR}
                            git pull origin main
                            python3 -m venv comp314
                            source comp314/bin/activate
                            python3 -m pip install -r requirements.txt
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
