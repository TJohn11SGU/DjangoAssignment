pipeline {
    agent any

    environment {
<<<<<<< HEAD
        EC2_USER = "ubuntu"  // Or ubuntu, depending on your AMI
        EC2_HOST = "3.135.193.246" //(MODIFY)
        EC2_KEY = credentials('ec2-ssh-private-key')  // Jenkins credential with SSH private key (MODIFY)
        PROJECT_DIR = "/home/ubuntu/myproject"  // Path to your Django app (MODIFY)
        
    }

    //triggers {
      //  githubPush()  // Enables webhook triggering
    //}
    
=======
        EC2_USER = "ubuntu"                     // SSH user for EC2
        EC2_HOST = "3.135.193.246"              // EC2 public IP
        EC2_KEY = credentials('ec2-ssh-private-key')  // Jenkins SSH key credential
        PROJECT_DIR = "/home/ubuntu/DjangoAssignment" // Django project path
    }

>>>>>>> 6ac4eb728afa9360926482bf1c113bca1c03f5a6
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
<<<<<<< HEAD
                            python3 manage.py migrate
                            python3 manage.py collectstatic --noinput
                            sudo systemctl restart gunicorn
=======
>>>>>>> 6ac4eb728afa9360926482bf1c113bca1c03f5a6
                        '
                        """
                    }
                }
            }
        }
    }

    post {
        success {
<<<<<<< HEAD
            echo "Code updated and app restarted successfully on EC2!"
        }
        failure {
            echo "Deployment failed."
=======
            echo "✅ Code updated and app restarted successfully on EC2!"
        }
        failure {
            echo "❌ Deployment failed. Check Jenkins logs for errors."
            slackSend color: 'danger', message: "Deployment failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
>>>>>>> 6ac4eb728afa9360926482bf1c113bca1c03f5a6
        }
    }
}
