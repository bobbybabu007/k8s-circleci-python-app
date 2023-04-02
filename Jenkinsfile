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
                echo 'Build $BUILD_ID is complete' > file.txt
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Archive the artifacts') {
            steps {
                echo 'Archiving....'
                archiveArtifacts artifacts: 'file.txt', followSymlinks: false, onlyIfSuccessful: true
            }
        }
        stage('Deploying') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
