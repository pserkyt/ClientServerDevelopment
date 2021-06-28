from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:35793/AAC' % (username, password))
        self.database = self.client['AAC']
        print(self.database)

    # Implement the C in CRUD: (returns True or False)
    def create(self, data):
        if data is not None:
            return self.database.animals.insert_one(data).acknowledged
        else:
            raise Exception("Nothing to insert, because data parameter is empty")
            return False

    # Implement the R in CRUD: (returns cursor)
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False}) # read without _id
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            return None

    # Implement the U in CRUD: (returns updated data)
    def update(self, data, data_updated):
        if data is not None:
            # update the value of the data dictionary into animal table
            result = self.database.animals.update_one(data, data_updated)
            # if update successful, return the updated data:
            if result.modified_count > 0:
                return self.read(data)
            else:
                print(result)
                return None
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            return None

    # Implement the D in CRUD: (returns True or False)
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_one(data)
            if result.deleted_count != 0:
                return True
            else:
                print(result)
                return False
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            return False

