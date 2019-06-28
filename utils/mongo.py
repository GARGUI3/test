""" Mongo module """
import os

from bson import ObjectId
from pymongo import MongoClient, DESCENDING, ASCENDING

__MONGO = {'client': None, 'database': None}

CONNECTED_STATUS_STRING = 'CONNECTED'

def get_mongo_collection(collection):
    """ Returns a collection from mongo """
    # Avoid to create multiples connections
    if not __MONGO['client']:
        mongo_client = MongoClient(os.environ['urlMongo'])
        mongo_db = mongo_client[os.environ['dataBaseMongo'].rstrip()]
        __MONGO['client'] = mongo_client
        __MONGO['database'] = mongo_db
    return __MONGO['database'].get_collection(collection)


def find_data(collection, query):
    """ Return list of users """
    user_collection = get_mongo_collection(collection)
    documents = user_collection.find(query)
    return documents

def disconnect():
    """ Decorator to close mongo connection """
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            _disconnect()
            return result
        return wrapper
    return decorator
