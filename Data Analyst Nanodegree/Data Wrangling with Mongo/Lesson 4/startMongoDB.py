from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.examples

autos = db.autos.find({"manufacturer" : "Toyota"})

for a in autos:
    print a
