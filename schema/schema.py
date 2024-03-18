from pydantic import BaseModel,Field


class ValidatePost(BaseModel):
    name:str=Field(...,description="name of person as a string")
    age:int=Field()

class ValidateUpdate(BaseModel):
    name:str=Field(...,description="name to update the age to zero")
    age:int

class ValidateDelete(BaseModel):
    name:str=Field(...,description="corresponding data with the name will be deleted")

