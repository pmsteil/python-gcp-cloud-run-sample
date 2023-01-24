# deploy.sh

project_id=`gcloud config get-value project`
region=us-west4
# imagename=image_brandx-api-py
# repo=cloud-run-source-deploy
# repopath=$region-docker.pkg.dev/$project_id/$repo
# image_fq=$repopath/$imagename

gcloud run deploy docker-brandx-api-py --source . --region $region --allow-unauthenticated --platform managed