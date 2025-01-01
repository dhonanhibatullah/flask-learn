from pymongo import MongoClient
from pymongo.database import Database
from utils.config import CONFIG

REQUIRED_COLLECTIONS = [
    'init',
    'users'
]

mdb = MongoClient(CONFIG['MONGO_URI'])[CONFIG['MONGO_DB']]
collections = mdb.list_collection_names()

for collection in REQUIRED_COLLECTIONS:
    if collection not in collections:
        mdb.create_collection(collection)

def get_db() -> Database:
    return mdb