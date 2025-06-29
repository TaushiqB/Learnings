from pydantic import BaseModel

# This is a Schema that is powered by Pydatic for type Hinting and data validation.
class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = { 'id': 1, 'name': "Taushiq", "is_active": True}
input_data2 = { 'id': 2, 'name': "Taushiq", "is_active": 'True'}
input_data3 = { 'id': 3, 'name': "Taushiq", "is_active": 1}
input_data4 = { 'id': 4, 'name': "Taushiq", "is_active": '1'}
input_data5 = { 'id': '5', 'name': "Taushiq", "is_active": True}
input_data6 = { 'id': 6, 'name': "Taushiq", "is_active": '5'}

user = User(**input_data)
user2 = User(**input_data2) # Pydantic will convert True to boolean
user3 = User(**input_data3) # Pydantic will convert 1 to boolean
user4 = User(**input_data4) # Pydantic will convert '1' to boolean
user5 = User(**input_data5) # Pydantic will convert '5' to int

print(user)
print(user2)
print(user3)
print(user4)
print(user5)