#Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

        
    def __init__(self,user,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:30128'%(user,password))
        self.database = self.client['AAC']
        
        
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            print("++++++++++++++++++ Inserting New Animal+++++++++++++++")
        else:
            raise Exception("Failed to add Data")
            
            
    # Complete this read method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            data = self.database.animals.find(data,{"_id":False})  # data should be dictionary   
            return data
        else:
            raise Exception("nothing to read, hint is empty")
            
            
    # Complete this delete method to implement the D in CRUD.
    def delete(self, _data):
        if _data is not None:
            data = self.read(_data) # checj if animal exists
            if data is None:
                print("Animal not found")
                return
            #if found delete the animal or animals
            self.database.animals.delete_many(_data)  # data should be dictionary 
            data = self.read(_data) #confirm if animal was deleted
            return data
        else:
            raise Exception("nothing to read, hint is empty")
            
    # Complete this update method to implement the U in CRUD.
    def update(self, _keys,_data):
        if _data is not None and _keys is not None:
            self.database.animals.update_many(_keys,{'$set':_data})  # _keys will check for the doc to update 
            data = self.read(_data)
            return data
        else:
            raise Exception("Please enter both key and data to modify the collection")