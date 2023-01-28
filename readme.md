# Docs

## todos
* get local/run to authenticate with google
* get lbin/run to use local code volume
* setup pytest unit testing
* should we use the locally built image and upload to gcloud?
    * gcloud beta run deploy [SERVICE_NAME] --image gs://[BUCKET_NAME]/[IMAGE_NAME]

## local docker commands
    local/run - build and run the project in local docker
    local/stop - stop the container
    local/start - start it again
    local/bash - get a command line to it
    local/logs - display running logs
    
    ./benchmarks.sh local 10 0 1


## local testing
    test/hello local
    test/post local
    test/benchmarks local
    test/benchmarks local 10 0 1    
    test/benchmarks local 1000 1 0

## remote testing
    test/hello remote
    test/post remote
    test/benchmarks remote
    test/benchmarks remote 10 0 1    
    test/benchmarks remote 1000 1 0

## GCP Deploy
    ./deploy.sh

## commands issued on this project
* gcloud auth application-default login
* gcloud services enable pubsub.googleapis.com
* pip install --upgrade google-cloud-pubsub
* gcloud services enable cloudprofiler.googleapis.com


## pubsub commands
* gcloud pubsub topics create test-topic
* gcloud pubsub subscriptions list
* gcloud pubsub subscriptions create py-test-subscription --topic test-topic
* gcloud pubsub subscriptions create py-test-subscription2 --topic test-topic
* gcloud pubsub subscriptions create py-test-push --topic test-topic --push-endpoint https://docker-brandx-api-py-jflup3ylrq-wn.a.run.app/pubSubProcessBCImport