pipeline {
    agent any
    stages {
        stage('SCM') {
            steps {
                echo 'Cloning..'
                git branch: 'main', changelog: false, poll: false, url: 'https://github.com/bobbybabu007/k8s-circleci-python-app'
            }
        }
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
