import pymongo
import certifi


mongo_url = "mongodb+srv://markomer:1qazxcvbBVCXZAQ!@cluster0.85lg4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

db = client.get_database("ArtVenue")