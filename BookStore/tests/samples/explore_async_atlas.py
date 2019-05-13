import pymongo
import dns # required for connecting with SRV
from pymongo.errors import ConnectionFailure


# ensure TLS/SSL extensions are there for pymongo
# python -m pip install pymongo[tls]
# python -c "import requests; print(requests.get('https://www.howsmyssl.com/a/check', verify=False).json()['tls_version'])"

###### Porting to Motor + Tornado for async performance ##########
# pip3 install tornado motor
import motor
import tornado.web
from tornado.ioloop import IOLoop



mongodbSvr1 = "mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test" # Senthil's DB
mongodbSvr2 =  "mongodb+srv://cmpe272:cmpe272@cmpe272-f1ptm.mongodb.net/test" # Yuva's DB
APIKey2 =  "00d64d13-3501-4760-8b9b-62dfe692aa21" # Yuva's DB

# Ref: https://motor.readthedocs.io/en/stable/tutorial-tornado.html 
# Ref: https://www.tornadoweb.org/en/stable/guide/structure.html 
# Ref: https://dzone.com/articles/motor-asynchronous-mongodb 
# Ref: https://stackoverflow.com/questions/30782113/how-to-pass-params-to-python-tornado-ioloop-run-syncmain-function


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        db = self.settings['db']        # setting member variable through external reference!

def make_app(db):
    # application = tornado.web.Application([
    #     (r'/', MainHandler)
    #     ])
    application = tornado.web.Application([
        (r'/', MainHandler)             #routes from main web page --> mapped to Handlers
        ])
    application.settings['db'] = db
    return(application)

async def check_ismaster(client):
    # try:
        # The ismaster command is cheap and does not require auth.
        c= await client.admin.command('ismaster')
        print("Server ismaster check result %s"% repr(c))
    # except ConnectionFailure:
        # https://docs.atlas.mongodb.com/driver-connection/#driver-examples
        #   + mongodb Atlas needs certs open "/Applications/Python 3.7/Install Certificates.command"
        #   + whitelist for ALL IPs v: works
        #   + restricted whitelist --> From Atlas use "current IP" for external facing IP
        #   ++ Also using "whats my ip" on google will give the right IP!!
        # print("Server not available %s" % repr(ConnectionFailure))


async def do_count(col):
    c = await col.count_documents({})
    print ("count %s"% repr(c))


async def do_insert(col):
    r1 = {'_id': '1', 'title': 'A test book'}
    # r2 = {'_id': '2', 'title': 'Another test book'}
    result = await col.insert_one(r1)
    print('result %s' % repr(result.inserted_id))





if __name__ == "__main__":
    client= motor.motor_tornado.MotorClient(mongodbSvr2)


    db=client.warriors_bookstore # "."-notation for db
    # #print(db.collection_names)
    col=db.war_books 

    # web-server code
    app = make_app(db)
    app.listen(8888)

    IOLoop.current().run_sync(lambda: check_ismaster(client)) #check if DB conection works
    IOLoop.current().run_sync(lambda: do_count(col)) # two parameter trick!
    IOLoop.current().run_sync(lambda: do_insert(col)) # add a record test





#^^ There are two things to note in this code. 
#   First, the MotorClient constructor doesn’t actually connect to the server; 
#       the client will initiate a connection when you attempt the first operation. 
#   Second, passing the database as the db keyword argument to Application 
#       makes it available to request handlers:



###### PyMongo code ###############

# # client = pymongo.MongoClient(mongodbSvr2,ssl=True)
# # db = client.test

# myclient = pymongo.MongoClient(mongodbSvr1)
# #try:
#     # The ismaster command is cheap and does not require auth.
# myclient.admin.command('ismaster')
# #except ConnectionFailure:
#     #print("Server not available")

# mydb = myclient["warriors_bookstore"] # connect to existing db
# mycol = mydb["war_books"] # connect to existing collection

# mydb.collection_names

# # x=mycol.find()

# # for y in x:
# #     print("Value")
# #   	#print(y)