from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

# Dump and Dump Json - Two types - How these models are used with Pydantic
# 

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_At: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime : lambda v: v.strftime
        ('%d-%m-%Y %H:%M:%S')}   # This is Used to format The Datetime shit  
    )

# Create an User Instance 
user = User(
     id = 1,
     name = "Taushiq",
     email = "taushiwhideh",
     created_At = datetime(2024, 3, 15, 14, 30),
     address = Address(
         street = "bkaajd",
         city = "Delhi",
         zip_code = "00"
     ),
     is_active = False,
     tags = ["premium", "subscriber"]
)

# Actual Serialization Code 
# Using Model_dump() -> Dictionary is the output
python_dict = user.model_dump()
print(python_dict)

# Using Model_dump_json() -> JSON Strings
json_str = user.model_dump_json()
print(json_str) # in the strong format the datetime is as - 2024-03-15T14:30:00
# TO change that we need to write customized model config 
# This will change due to the change json Encoders