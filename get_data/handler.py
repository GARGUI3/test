'''
Module get users
'''
from utils import mongo

COLLECTION = 'users'

@mongo.disconnect()
def main(event, context):
    ''' List top authors with more proposals '''
    query = {}

    users = mongo.find_data(COLLECTION, query)

    return users
