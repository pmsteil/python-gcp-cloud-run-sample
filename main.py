import os
import time
import random

from flask import Flask


from google.cloud import pubsub_v1
# from concurrent.futures import TimeoutError


project_id="moonlit-ceiling-347716"
app = Flask(__name__)







@app.route("/")
def root():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)





@app.route("/hello")
def hello( ):
    
    # get name from a request parameter
    # name = request.args.get("name", name)

    # return hello name with carraige return
    return "Hello World!\n"
    




#-------------------------------------------------------
# api route for pubSubProcessBCImport
#
#    https://cloud.google.com/pubsub/docs/samples/pubsub-create-push-subscription#pubsub_create_push_subscription-python
#    
#-------------------------------------------------------
@app.route("/pubSubProcessBCImport", methods=['POST'])
def pubSubProcessBCImport(request=None, message=None):

    # name = os.environ.get("ENVIRONMENT", "STAGING")

    # if request is None: return an error 500
    if request is None:
        return "Error: `request` not received\n", 500
    
    
    # print request variables
    print("request: {}".format(request))
    print("message: {}".format(message))
    # print("request.args: {}".format(request.args))
    # print("request.form: {}".format(request.form))
    # print("request.data: {}".format(request.data))
    # print("request.headers: {}".format(request.headers))
    # print("request.message: {}".format(request.message))
    # print("request.method: {}".format(request.method))
    # print("request.url: {}".format(request.url))

    
    # message_data = message.data 
    # print("Received message: {}".format(message_data)) 
    
    # track time of execution of this function    
    start = time.time()




    # wait for a random time between 1 and 5 seconds
    if( 0 ):
        time.sleep(random.randint(1,4))
    

    end = time.time()
    
    # flip a coin to determine if we should return an error
    if( 0 ):
        if random.randint(0,1) == 0:
            return "Error: BCImport 'random' failure\n", 500

    return "BCImport completed [{}s]\n".format(end - start)

# add api route to be called by pubSub to process BCImport messages
app.add_url_rule("/pubSubProcessBCImport", "pubSubProcessBCImport", pubSubProcessBCImport, methods=["POST"])






#-------------------------------------------------------
# api route for ProcessMi9Import
#-------------------------------------------------------
@app.route("/pubSubProcessMi9Import")
def pubSubProcessMi9Import():
    # track time of execution of this function
    
    start = time.time()

    # name = os.environ.get("ENVIRONMENT", "STAGING")

    # wait for a random time between 1 and 3 seconds
    time.sleep(random.randint(1,3))
    end = time.time()

    # flip a coin to determine if we should return an error
    if random.randint(0,1) == 0:
        return "Error: Mi9Import 'random' failure\n", 500

    return "Mi9Import completed [{}s]\n".format(end - start)



#-------------------------------------------------------
# api route for createPubSubMessages
#-------------------------------------------------------
@app.route("/createPubSubMessages")
def createPubSubMessages():
    
        
    topic_id = "test-topic"
    published_messages = 0 

    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)

    for n in range(1, 10):
        data = f"Python message number {published_messages}"
        # Data must be a bytestring
        data = data.encode("utf-8")
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data)
        published_messages += 1
        # print(future)
        print(future.result())

    return "Published {} messages to {}.\n".format( published_messages, topic_path )






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

