from fastapi import APIRouter,Body,Header
from schema import schema
from database import db
from fastapi.encoders import jsonable_encoder
router = APIRouter()
#CRUD
@router.post('/postdata')
def postData(data:schema.ValidatePost=Body(...,description="insert data to db")):
    return db.add_Data(jsonable_encoder(data))


@router.get('/showdata')
def showData(str=Header("show data")):
   return db.show_Data()

@router.put('/update')
def updateData(data:schema.ValidateUpdate=Body(...,description="set age of particular name to zero")):
    return db.update_Data(data)

@router.delete('/deleteuser')
def deleteData(data:schema.ValidateDelete=Body(...,description="delete user with name porvided")):
    return db.delete_Data(data)
