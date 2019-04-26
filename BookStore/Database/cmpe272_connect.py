import pymongo
import dns # required for connecting with SRV

mongodbSvr2 =  "mongodb+srv://cmpe272:cmpe272@cmpe272-f1ptm.mongodb.net/test?retryWrites=true" # Yuva's DB

myclient = pymongo.MongoClient(mongodbSvr2)
mydb = myclient["warriors_bookstore"]
