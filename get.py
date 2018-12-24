import pymongo
import datetime

calix = 0
if calix == 1:
    #myclient = pymongo.MongoClient("mongodb://localhost:4000/")
    uri = "mongodb://activate:pmaa123@127.0.0.1:4000/activate"
    myclient = pymongo.MongoClient(uri)
    print("Sucessfully Connected to the Database")
else:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["activate"]
mycol = mydb["AuditLogNotSecured"]
#details = mycol.find({ "$and": [ {"changeLog": { "$gt": 15000 }}, {"changeLog": { "$lt": 16001 }}] })

allStart = datetime.datetime.now()

startRecord = 4500000

#pagination
skip = 0
step = 1000
#check for 5 iterations
for i in range(1):
    print("Iteration No: " + str(i))
    print("Start Time: " + str(datetime.datetime.now()))
    print("Skip: " + str(skip) + " Step: " + str(step))
    details = mycol.find().skip(startRecord + skip).limit(step)
    cnt = details.count(True)
    print("Total records retrived: " + str(cnt))

    skip += step
    for record in details:
        print("clientIP: " + str(record["clientIP"]))
        record["clientIP"]
    print("End Time:" + str(datetime.datetime.now()))

allEnd = datetime.datetime.now()
duration = allEnd - allStart

print("Start: " + str(allStart))
print("End  : " + str(allEnd))
print("Total records processed: " + str(skip))
print("Duration(seconds:milliseconds): " + str(duration.seconds) + "." + str(duration.microseconds/1000))


allrecords = mycol.find()
print("Total rescords in the collection is : " + str(allrecords.count()))
