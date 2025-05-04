from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb+srv://DBADMIN:dbadmin@identity-srv.tczupwg.mongodb.net/?retryWrites=true&w=majority&appName=identity-srv")

db = client.user_identity_db

collection_name = db["user_identity_collection"]