import pymongo
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["activate"]
mycol = mydb["AuditLogNotSecured"]

startTime = datetime.datetime.utcnow().isoformat()
endTime = datetime.datetime.utcnow().isoformat()

st  = mycol.count()
print(st)

for ctr in range(st, st + 2):
    mydict = {
        "className" : "com.calix.app.AuditLogNotSecured",
        "clientIP" : "127.0.0.1",
        "emsServerIP" : "172.23.51.109",
        "startTime" : startTime,
        "endTime" : endTime,
        "user" : "admin",
        "operationType" : "Retrieve Domain List",
        "description" : " Retrieving Domain List  admin   ,  Status  is OK",
        "tokenId" : "TqqFdutEJWQWCwofEB",
        "changeLog" : ctr,
        "timestamp" : 1.0,
        "uid" : "6f9ba9e5-3358-475c-8352-b459b4272ead",
        "autocompeleteDesc" : "",
        "webURL" : "",
        "creationDate" : startTime,
        "lastChange" : endTime,
        "domainIdList" : [
                "DEFAULT"
        ],
        "version" : 1.0
    }

    x = mycol.insert_one(mydict)
    if ctr % 1000 == 0:
        print("inserted " + str(ctr) + " records")

