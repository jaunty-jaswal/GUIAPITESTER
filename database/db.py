import pymongo
from fastapi import HTTPException,status
from bson import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()
MONGO_CLIENT = os.getenv('KEY')
client = pymongo.MongoClient( MONGO_CLIENT)
db_name = client["Test"]
collection = db_name["test_"]

def parser(data):
    return {
        "name":data["name"],
        "age":data["age"]
    }

def add_Data(data):
    check = collection.insert_one(data)
    if check:
        return {"Response":HTTPException(status_code=status.HTTP_200_OK)}
    else:
        return {"Response":HTTPException(status_code=status.HTTP_404_NOT_FOUND)}

    
def show_Data():
    var = list()
    for i in collection.find():
        if isinstance(i["_id"] ,ObjectId):
            # i["_id"] = str(i["_id"])
            # i.pop("_id",None)
            var.append(parser(i))
    return var        

def update_Data(data):
    if(collection.find_one({"name":data.name})):
       collection.update_one({"name":data.name},{"$set":{"age":data.age}})
       return {"Response":HTTPException(status_code=status.HTTP_200_OK)}
    else:
       return {"Response":HTTPException(status_code=status.HTTP_404_NOT_FOUND)}

def delete_Data(data):
    if(collection.find_one({"name":data.name})):
        collection.delete_one({"name":data.name})
        return {"Response":HTTPException(status_code=status.HTTP_202_ACCEPTED)
                }
    else:
        return {"Response":HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)}


