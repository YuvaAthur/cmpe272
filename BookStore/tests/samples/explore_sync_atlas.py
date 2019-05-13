import pymongo
import dns # required for connecting with SRV
from pymongo.errors import ConnectionFailure

mongodbSvr1 = "mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test" # Senthil's DB
mongodbSvr2 =  "mongodb+srv://cmpe272:cmpe272@cmpe272-f1ptm.mongodb.net/test" # Yuva's DB
APIKey2 =  "00d64d13-3501-4760-8b9b-62dfe692aa21" # Yuva's DB


def check_ismaster(client):
    # try:
        # The ismaster command is cheap and does not require auth.
        # make sure that Current IP is in whitelist list of Atlas Cluster
        c= client.admin.command('ismaster')
        print("Server ismaster check result %s"% repr(c))
    # except ConnectionFailure:
        # https://docs.atlas.mongodb.com/driver-connection/#driver-examples
        #   + mongodb Atlas needs certs open "/Applications/Python 3.7/Install Certificates.command"
        #   + whitelist for ALL IPs v: works
        #   + restricted whitelist --> From Atlas use "current IP" for external facing IP
        #   ++ Also using "whats my ip" on google will give the right IP!!
        # print("Server not available %s" % repr(ConnectionFailure))

def do_insert(col):
    r1 = {'_id': '1', 'title': 'A test book'}
    # r2 = {'_id': '2', 'title': 'Another test book'}
    result =  col.insert_one(r1)
    print('result %s' % repr(result.inserted_id))

def do_count(col):
    c =  col.count_documents({})
    print ("count %s"% repr(c))

if __name__ == "__main__":
    client = pymongo.MongoClient(mongodbSvr2)
    db = client["test_bookstore"]
    col = db["books"]

    check_ismaster(client)
    do_insert(col)
    do_count(col)

