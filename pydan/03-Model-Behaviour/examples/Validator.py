# Model Validator and Field Validator
from pydantic import BaseModel, field_validator, model_validator, computed_field
# Field Validator is for customized validation

class User(BaseModel):
    Username: str
