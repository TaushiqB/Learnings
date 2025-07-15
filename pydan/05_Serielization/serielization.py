from pydantic import BaseModel
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    name: str
    email: str
    is_active: bool = True
    created_At: datetime
    address: Address
    tags: List[str] = []