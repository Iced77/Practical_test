pipeline {
  agent any
  stages {
    stage('OWASP DependencyCheck') {
      steps {
        dependencyCheck additionalArguments: '--format HTML --format XML --noupdate ', odcInstallation: 'OWASP Dependency-Check Vulnerabilities'
      }
    }
  }  
  post {
    success {
      dependencyCheckPublisher pattern: 'dependency-check-report.xml'
    }
  }
}
