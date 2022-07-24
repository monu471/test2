import pymongo
client = pymongo.MongoClient("mongodb+srv://monu:monu471@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name": "sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}
db1 = client['mongo']
coll = db1['test']
coll.insert_one(d)

d = {
    "name": "sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}
db1 = client['mongo']
coll = db1['test']
coll.insert_one(d)
d = {
    "name": "sudhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname": "kumar"
}
db1 = client['mongo']
coll = db1['test']
coll.insert_one(d)

