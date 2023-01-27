# deploy.sh
clear

# prebuld checks
echo
echo "----------------------------------------------------------------------------"
echo "| Precompiling...                                                          |"
echo "----------------------------------------------------------------------------"

pyflakes=$(pyflakes main.py)

# if pyflakes returns an error, exit
if [ $? -ne 0 ]; then        
    echo "| ERROR pyflakes syntax check failed, please resolve errors and try again..."
    echo "----------------------------------------------------------------------------"
    echo "| $pyflakes"
    echo "----------------------------------------------------------------------------"

    exit 1
else
    echo "| passed...                                                                |"
    echo "----------------------------------------------------------------------------"
fi






project_id=`gcloud config get-value project`
region=us-west4
# imagename=image_brandx-api-py
# repo=cloud-run-source-deploy
# repopath=$region-docker.pkg.dev/$project_id/$repo
# image_fq=$repopath/$imagename

pip3 freeze > requirements.txt
gcloud run deploy docker-brandx-api-py --source . --region $region --allow-unauthenticated --platform managed --memory 128Mi --cpu 2 --max-instances 5 --min-instances 0 


