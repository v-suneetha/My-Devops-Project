pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/v-suneetha/My-Devops-Project.git'
                bat 'echo %COMSPEC%'
            }
        }
        stage('Replica to zero')
            {
                steps{
                    bat 'kubectl scale deployment java-api --replicas=0'
                    bat 'kubectl scale deployment python-alert --replicas=0'
                }
            }

        stage('Deploy to Kubernetes') {
            steps {
                    dir('java-api'){
                    bat 'kubectl apply -f deployment.yaml'
                    bat 'kubectl apply -f service.yaml'
                    }
                    dir('python-alert')
                    {
                     bat 'kubectl apply -f deployment.yaml' 
                     bat 'kubectl get pods'
                     bat 'kubectl get svc'
                     }
            }
            }

            stage('Get Java-api Logs') {
            steps {
                bat '''
                for /F "tokens=1" %%i in ('kubectl get pods -o custom-columns^=NAME:.metadata.name --no-headers ^| findstr java-api') do kubectl logs %%i
                '''
            }
        }
        stage('Get python-alert Logs') {
            steps {
                bat '''
                for /F "tokens=1" %%i in ('kubectl get pods -o custom-columns^=NAME:.metadata.name --no-headers ^| findstr python-alert') do kubectl logs %%i
                '''
            }
        }

        
    }
}
