# Docs

## local testing
    python3 main.py
    ./benchmarks.sh local 10 0 1

## GCP Deploy
    ./deploy.sh

## remote testing
    ./benchmarks.sh remote 10 0 1
    ./benchmarks.sh remote 1000 1 0


## commands issued on this project
gcloud services enable pubsub.googleapis.com
pip install --upgrade google-cloud-pubsub