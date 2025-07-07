# Model Validator and Field Validator
from pydantic import BaseModel, field_validator, model_validator, computed_field
# Field Validator is for customized validation

class User(BaseModel):
    Username: str

    @field_validator('username') # Field validators run before the pydantic model - Automatically
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be atleast 4 Characters")
        return v
    
class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after') # Works after all the custom validations
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password Do not Match')
        return values
    
class Product(BaseModel):
    price: float
    quantity: int

    @computed_field # Creates a new property
    @property
    def total_price(self)->float:
        return self.price * self.quantity

