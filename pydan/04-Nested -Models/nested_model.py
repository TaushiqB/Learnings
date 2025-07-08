from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address # Nested model referrencing, this class is referring to the previous class

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None   # This is self referrencing - this is called forward referrencing

Comment.model_rebuild() # This is needed for forward referrencing

address = Address(
    street = "123, something",
    city = "Jaipur",
    postal_code = "10001"
)

user = User(
    id = 1, 
    name = "Taushiq", 
    address = address
)

comment = Comment(
    id = 1,
    content="First Comment",
    replies = [
        Comment(id=2, content = "Reply1"),
        Comment(id=3, content="reply2")
    ]
)