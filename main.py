import os
import time
import random



from flask import Flask

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
#-------------------------------------------------------
@app.route("/pubSubProcessBCImport")
def pubSubProcessBCImport( message ):
    
    # message_data = message.data 
    # print("Received message: {}".format(message_data)) 
    
    # track time of execution of this function    
    start = time.time()

    name = os.environ.get("ENVIRONMENT", "STAGING")



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
@app.route("/ProcessMi9Import")
def ProcessMi9Import():
    # track time of execution of this function
    
    start = time.time()

    name = os.environ.get("ENVIRONMENT", "STAGING")

    # wait for a random time between 1 and 3 seconds
    time.sleep(random.randint(1,3))
    end = time.time()

    # flip a coin to determine if we should return an error
    if random.randint(0,1) == 0:
        return "Error: Mi9Import 'random' failure\n", 500

    return "Mi9Import completed [{}s]\n".format(end - start)















if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))