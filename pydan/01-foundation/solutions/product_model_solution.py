from pydantic import BaseModel

class product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True  # Defaukt Value True Added

input_data = {'id': 1, 'name':"Taushiq", 'price': 2000.00, 'in_stock': True}

prod = product(**input_data)

print(prod)