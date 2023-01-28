# Docs

## todos
* setup pytest unit testing
* should we use the locally built image and upload to gcloud?
    * gcloud beta run deploy [SERVICE_NAME] --image gs://[BUCKET_NAME]/[IMAGE_NAME]

## local testing
    <!-- python3 main.py -->
    local/run
    local/test local
    
    ./benchmarks.sh local 10 0 1

## GCP Deploy
    ./deploy.sh

## remote testing
    ./benchmarks.sh remote 10 0 1
    
    ./benchmarks.sh remote 1000 1 0


## commands issued on this project
* gcloud auth application-default login
* gcloud services enable pubsub.googleapis.com
* pip install --upgrade google-cloud-pubsub


## pubsub commands
* gcloud services enable cloudprofiler.googleapis.com
* gcloud pubsub topics create test-topic
* gcloud pubsub subscriptions list
* gcloud pubsub subscriptions create py-test-subscription --topic test-topic
* gcloud pubsub subscriptions create py-test-subscription2 --topic test-topic
* gcloud pubsub subscriptions create py-test-push --topic test-topic --push-endpoint https://docker-brandx-api-py-jflup3ylrq-wn.a.run.app/pubSubProcessBCImport