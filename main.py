import os
import time
import random

import json
# import Service

# import inspect for function introspection
import inspect

from google.cloud import pubsub_v1


# load environment variables from .env file
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# load environment variables
PROJECT_ID                  = os.getenv('PROJECT_ID')
FLAG_ADD_RANDOM_DELAY       = bool(int(os.getenv('FLAG_ADD_RANDOM_DELAY')))
FLAG_RETURN_RANDOM_ERRORS   = bool(int(os.getenv('FLAG_RETURN_RANDOM_ERRORS')))
print( f"Server started - project_id: {PROJECT_ID}" )
print( f"FLAG_ADD_RANDOM_DELAY: {FLAG_ADD_RANDOM_DELAY}" )
print( f"FLAG_RETURN_RANDOM_ERRORS: {FLAG_RETURN_RANDOM_ERRORS}" )



# authenticdate with google cloud
# https://cloud.google.com/docs/authentication/getting-started
# https://cloud.google.com/docs/authentication/production
# https://cloud.google.com/docs/authentication/production#auth-cloud-implicit-python
# https://cloud.google.com/docs/authentication/production#auth-cloud-explicit-python
# pip3 install google-cloud-logging
# from google.cloud import logging
# logging_client = logging.Client()
# logger = logging_client.logger('my-log')
# logger.log_text('SERVER STARTED!')



from flask import Flask,request
app = Flask(__name__)










@app.route("/hello")
def hello( ):
    
    # get name from a request parameter
    # name = request.args.get("name", name)

    # return hello name with carraige return
    return "Hello World!\n"
    





# process_check_catalogs
# process_queue_up_catalog_products
# process_queue_up_catalog_report

# process_bcimport
# process_bcsync
# process_bcimage

# process_mi9import

# process_import_log
# process_xdb_log



#-------------------------------------------------------
# API endpoint: /process_bcimport
#    This endpoint will have messages pushed to it
#    by the pubsub topic called `bcimport`
#-------------------------------------------------------
@app.route("/process_bcimport", methods=['POST'])
def process_bcimport():

    # track time of execution of this function
    start = time.time()
   
    api_name = inspect.currentframe().f_code.co_name + "::"
   
    # pull the posted data from the request
    data = json.loads(request.data)

    # if product_id is not in the data, return an error
    if 'product_id' not in data['message']:
        return "Error: `product_id` not received\n", 500
    
    if 'catalog_id' not in data['message']:
        return "Error: `catalog_id` not received\n", 500

    # retrieve the fields from the data
    product_id = data['message']['product_id']
    catalog_id = data['message']['catalog_id']

    # format the return data    
    returndata = f"product_id: {product_id}, catalog_id: {catalog_id}"
    print( f"{api_name}received ==> {returndata}" )


    # wait for a random time between 1 and 5 seconds
    if( FLAG_ADD_RANDOM_DELAY ):
        print( f"{api_name}random delay added: {FLAG_ADD_RANDOM_DELAY}" )
        time.sleep(random.randint(1,4))
        
    
    # flip a coin to determine if we should return an error
    if( FLAG_RETURN_RANDOM_ERRORS ):
        if random.randint(0,1) == 0:
            print( f"{api_name}random error tripped {FLAG_RETURN_RANDOM_ERRORS}" )
            return "Error: BCImport 'random' failure\n", 500

    end = time.time()
    

    return "{}completed [{}s] {}\n".format( api_name, end - start, returndata)





#-------------------------------------------------------
# api route for createPubSubMessages
#
#    https://cloud.google.com/pubsub/docs/samples/pubsub-create-push-subscription#pubsub_create_push_subscription-python
#    
#-------------------------------------------------------
@app.route("/createPubSubMessages", methods=['POST'])
def createPubSubMessages():
    
        
    topic_id = "test-topic"
    published_messages = 0 

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(PROJECT_ID, topic_id)

    for n in range(1, 10):
        data = f"Test message number {published_messages}"
        _queueMessage( topic_id, data )

        # # Data must be a bytestring
        # data = data.encode("utf-8")
        # # When you publish a message, the client returns a future.
        # future = publisher.publish(topic_path, data)
        # published_messages += 1
        # # print(future)
        # print(future.result())

    return "Published {} messages to {}.\n".format( published_messages, topic_path )



def _queueMessage( topic_id, message ): 
    
    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(PROJECT_ID, topic_id)
        
    # Data must be a bytestring
    message = message.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, message )
    message_id = future.result();    
    
    print( "_queueMessage( message_id {} on {}).\n".format( message_id, topic_id ) )

    return( message_id )





#-------------------------------------------------------
# api route for perfTest
#-------------------------------------------------------
@app.route("/perfTest1M")
def perfTest1M():
    
    # track time of execution of this function
    start = time.time()

    # 10,000,000 times, add a string to a list    
    mylist = []
    for i in range(1000000):
        mylist.append("Test string # " + str(i) )

    end = time.time()
        
    
    return "PY perfTest1M completed [{}s]\n".format(end - start)







#-------------------------------------------------------
# api route for perfTest
#-------------------------------------------------------
@app.route("/perfTest10M")
def perfTest10M():
    
    # track time of execution of this function
    start = time.time()

    # 10,000,000 times, add a string to a list    
    mylist = []
    for i in range(10000000):
        mylist.append("Test string # " + str(i) )

    end = time.time()
        
    
    return "PY perfTest10M completed [{}s]\n".format(end - start)







#-------------------------------------------------------
# api route for perfTest
#-------------------------------------------------------
@app.route("/perfTest100M")
def perfTest100M():
    
    # track time of execution of this function
    start = time.time()

    # 10,000,000 times, add a string to a list    
    mylist = []
    for i in range(100000000):
        mylist.append("Test string # " + str(i) )

    end = time.time()
        
    
    return "PY perfTest100M completed [{}s]\n".format(end - start)





















if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))










# @app.route('/success/<name>')
# def success(name):
#    return 'welcome %s' % name

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))

    








# Sure, here's an example of a Dataflow pipeline written in Python that reads data from a Cloud SQL instance, filters and transforms the data using a SQL query, and sends the data to a Pub/Sub topic:

# from google.cloud import dataflow as df
# from google.cloud.dataflow.io import JdbcSource
# from google.cloud.dataflow.io import PubsubSink

# #Create a pipeline object
# pipeline = df.Pipeline()

# #Read data from the Cloud SQL instance using JdbcSource
# products_table = pipeline | 'Read from Cloud SQL' >> JdbcSource(
#     query='SELECT * FROM products WHERE price > 100',
#     data_source_config=JdbcSource.DataSourceConfiguration(
#     jdbc_url='jdbc:mysql://<hostname>:<port>/<database>',
#     username='<username>',
#     password='<password>'))

# #Filter and transform the data using a SQL query
# transformed_data = products_table | 'Filter and Transform' >> df.Map(lambda x: x.replace('$',''))

# #Send the data to a Pub/Sub topic
# transformed_data | 'Send to Pub/Sub' >> PubsubSink(topic='<your-topic-name>')

# #Run the pipeline
# pipeline.run()

