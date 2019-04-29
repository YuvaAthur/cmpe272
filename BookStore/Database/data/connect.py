import pymongo
import dns # required for connecting with SRV

# ensure TLS/SSL extensions are there for pymongo
# python -m pip install pymongo[tls]
# python -c "import requests; print(requests.get('https://www.howsmyssl.com/a/check', verify=False).json()['tls_version'])"


mongodbSvr1 = "mongodb+srv://cmpe272:cmpe272@cluster0-g5aa2.mongodb.net/test" # Senthil's DB
mongodbSvr2 =  "mongodb+srv://cmpe272:cmpe272@cmpe272-f1ptm.mongodb.net/test?retryWrites=true" # Yuva's DB
APIKey2 =  "00d64d13-3501-4760-8b9b-62dfe692aa21" # Yuva's DB


client = pymongo.MongoClient("mongodb+srv://cmpe272:<password>@cmpe272-f1ptm.mongodb.net/test?retryWrites=true")
db = client.test

# myclient = pymongo.MongoClient(mongodbSvr1)
# mydb = myclient["warriors_bookstore"] # connect to existing db
# mycol = mydb["war_customers"] # connect to existing collection

# x=mycol.find()

# for y in x:
#   	print(y)