if [ "$1" = "local" ]; then
    baseuri=http://127.0.0.1:8080
    service=$1
elif [ "$1" = "remote" ]; then
    baseuri=https://docker-brandx-api-py-jflup3ylrq-wn.a.run.app
    service=$1    
fi

echo "Calling $baseuri/hello"
curl $baseuri/hello \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"message": {
    "product_id": "12345",
    "catalog_id": "54321"
  }}'