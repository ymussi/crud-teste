#!/usr/bin/groovy
//Jenkinsfile v7 2020-01-03
//Maintainer - infrastructure@captalys.com.br

env.APP = "zion-crud"
env.APP_SANDBOX = "zion-crud-sandbox"
env.APP_STAGING = "zion-crud-staging"

env.IMAGE_REPOSITORY = "harbor.captalysplatform.io/platform-v2/zion-crud"
env.HELM_REPO = "platform-v2"

env.NOTIFY = 0

def getBuildStages(enabled) {
  def stages = []
  if (enabled == 'false') {
    return stages
  }
  if (env.BRANCH_NAME == 'master') {
    env.TAG = 'prod-'
    env.ENV = 'production'
    env.FULL = '0'
    env.BUILD = '1'
    env.TARGET_APP = env.APP
    stages = ["tests", "build", "push artifact", "deploy"]
  }
//   else if ( env.BRANCH_NAME == 'sandbox') {
//     env.TAG = "sbox-"
//     env.ENV = "sandbox"
//     env.FULL = '1'
//     env.BUILD = '1'
//     env.NOTIFY = '1'
//     env.TARGET_APP = env.APP_SANDBOX
//     stages = ["tests", "code analysis", "build", "push artifact", "deploy"]
//   }
//   else if ( env.BRANCH_NAME == 'staging') {
//     env.TAG = "stag-"
//     env.ENV = "staging"
//     env.FULL = '1'
//     env.BUILD = '1'
//     env.TARGET_APP = env.APP_STAGING
//     stages = ["tests", "code analysis", "build", "push artifact", "deploy"]
//   }
//   else if ( env.BRANCH_NAME =~ '.hotfix.') {
//     env.TAG = "hotfix-"
//     env.ENV = "sandbox"
//     env.FULL = '1'
//     env.BUILD = '0'
//     stages = ["tests", "code analysis"]
//   }
//   else if ((env.BRANCH_NAME =~ '.*feature.*').matches()) {
//     env.TAG = "feature-"
//     env.ENV = "development"
//     env.FULL = '0'
//     env.BUILD = '0'
//     stages = ["tests"]
//   }
  else {
    env.BUILD = '0'
    env.FULL = '0'
    env.TAG = "other-"
    env.ENV = "development"
    stages = ["tests"]
  }
  return stages
}

// properties([[$class: 'GitLabConnectionProperty', gitLabConnection: 'GitLabCaptalys']])
// node('master') {
//   stage("Checkout") {
//     sh "rm -fr *"
//     checkout([
//       $class: 'GitSCM',
//       branches: scm.branches,
//       doGenerateSubmoduleConfigurations: scm.doGenerateSubmoduleConfigurations,
//       extensions: scm.extensions + [[$class: 'CloneOption', noTags: false, reference: '', shallow: false]],
//       submoduleCfg: [],
//       userRemoteConfigs: scm.userRemoteConfigs
//     ])
//     git_tag = sh(returnStdout: true, script: "git log | head -n 1 | cut -c8-15 ").trim()
//   }

  env.STATUS = sh(returnStdout: true, script: "gauntlet get-status -s ${env.APP}")
  gitlabBuilds(builds: getBuildStages(env.STATUS)) {

    env.TESTS = sh(returnStdout: true, script: "gauntlet get-tests -s ${env.APP}").trim()
    env.CHART_VERSION = sh(returnStdout: true, script: "gauntlet get-chart-version -c ${env.TARGET_APP}").trim() as Integer
    env.CLUSTER_CONTEXT = sh(returnStdout: true, script: "gauntlet get-context -s ${env.TARGET_APP}").trim()

    // if (env.TESTS == 'true'){
    //   docker.image('postgres:10.3').withRun("-e POSTGRES_PASSWORD=test -e POSTGRES_USER=test -e POSTGRES_DB=${env.APP}") { c->
    //     docker.image('harbor.captalysplatform.io/platform-v2/pytest:latest').inside("-u 109:113 -e TEST_DATABASE_URL=postgres://db:5432/${env.APP}?user=test&password=test --link ${c.id}:db") {
    //       stage("Tests") {
    //         gitlabCommitStatus(name: 'tests') {
    //           updateGitlabCommitStatus name: 'tests', state: 'running'
    //           try {
    //             module = sh(returnStdout: true, script:"cat setup.py | grep name= | cut -d'\"' -f2 | cut -d\"\'\" -f2").trim()
    //             sh "pip install -r requirements.txt --user && python setup.py develop --user"
    //             sh "python -m pytest --cov-config .coveragerc --cov=${module} test"
    //             double coverage_result = sh(returnStdout: true, script: "coverage report | grep TOTAL | grep -o '[[:digit:]]*%' | cut -d'%' -f1") as Double
    //             sh "coverage xml -o coverage.xml"
    //             if (coverage_result < 60) {
    //               zulipSend topic: "${env.APP}" , message: "Test coverage of ${coverage_result}% is below the allowed value of 60%. The app needs more tests."
    //               updateGitlabCommitStatus name: 'tests', state: 'success'
    //             }
    //             else {
    //               updateGitlabCommitStatus name: 'tests', state: 'success'
    //             }
    //           }
    //           catch (exc) {
    //             updateGitlabCommitStatus name: 'tests', state: 'failed'
    //             sh "exit 1"
    //           }
    //         }
    //       }
    //     }
    //   }
    // }
    // else {
    //   updateGitlabCommitStatus name: 'tests', state: 'success'
    // }
    // if (env.FULL == "1"){
    //   stage("Code Analysis") {
    //     gitlabCommitStatus(name: 'code analysis') {
    //       updateGitlabCommitStatus name: 'code analysis', state: 'running'
    //       try {
    //         sh "echo -e '\nsonar.projectVersion=${env.TAG}${git_tag}' >> sonar-project.properties"
    //         sh "sonar-scanner"
    //         sh "rm -fr coverage.xml"
    //         updateGitlabCommitStatus name: 'code analysis', state: 'success'
    //         zulipSend topic: "${env.APP}" , message: "Check ${env.APP}\'s code analysis for commit ${git_tag} on ${env.BRANCH_NAME} at https://sonarqube.captalysplatform.io/dashboard?id=${env.APP}"
    //       }
    //       catch (exc) {
    //         updateGitlabCommitStatus name: 'code analysis', state: 'failed'
    //         sh "exit 1"
    //       }
    //     }
    //   }
    // }
    if (env.BUILD == "1") {
    //   stage("Build Artifact") {
    //     gitlabCommitStatus(name: 'build') {
    //       updateGitlabCommitStatus name: 'build', state: 'running'
    //       try {
    //         sh "docker build --pull -t ${env.IMAGE_REPOSITORY}:${env.TAG}latest -t ${env.IMAGE_REPOSITORY}:${env.TAG}${git_tag} --build-arg RUN_ENVIRONMENT=${env.ENV} ."
    //         updateGitlabCommitStatus name: 'build', state: 'success'
    //       }
    //       catch (exc) {
    //         updateGitlabCommitStatus name: 'build', state: 'failed'
    //         sh "exit 1"
    //       }
    //     }
    //   }
    //   stage("Push Artifact") {
    //     gitlabCommitStatus(name: 'push artifact') {
    //       updateGitlabCommitStatus name: 'push artifact', state: 'running'
    //       try {
    //         sh "docker push ${env.IMAGE_REPOSITORY}:${env.TAG}${git_tag}"
    //         sh "docker push ${env.IMAGE_REPOSITORY}:${env.TAG}latest"
    //         updateGitlabCommitStatus name: 'push artifact', state: 'success'
    //       }
    //       catch (exc) {
    //         updateGitlabCommitStatus name: 'push artifact', state: 'failed'
    //         sh "exit 1"
    //       }
    //     }
    //   }
      stage('Promotion') {
        gitlabCommitStatus(name: 'push artifact') {
          updateGitlabCommitStatus name: 'deploy', state: 'running'
          try {
            stage("Deploy to ${env.ENV}") {
              sh "helm repo update"
              sh "helm upgrade ${env.TARGET_APP} ${env.HELM_REPO}/${env.TARGET_APP} --kube-context ${env.CLUSTER_CONTEXT} --install --namespace ${env.ENV} --version ${env.CHART_VERSION} --set image.tag=${env.TAG}${git_tag}"
              updateGitlabCommitStatus name: 'deploy', state: 'success'
            }
          }
          catch (exc) {
            updateGitlabCommitStatus name: 'deploy', state: 'failed'
            sh "exit 1"
          }
        }
      }
    }
  }
}
