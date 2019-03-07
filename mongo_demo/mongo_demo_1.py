import pymongo

# connect to database
client = pymongo.MongoClient()
# choose the database
test = client.test
# choose the collection
test1 = test.test1
# operate data
result = test1.find()
# for r in result:
#     print(r)

print(result.next())
# print(result.next())

# result = test1.find().sort("name", pymongo.DESCENDING)

# result = test1.find().limit()

# result = test1.find().count()

data = {"name": "kkz", "age": 18}
test1.insert_one(data)
