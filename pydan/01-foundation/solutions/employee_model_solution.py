from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int                                  # Integer
    Name: str = Field(                       # String Minimum 3 Characters
        ...,                                 # Three Dots indicate its a required a field
        min_length=3,                        # Minimum Length
        max_length=50,                       # Maximum Length
        description="Employee Name",         # Adds Description in Swagger UI (No Affect on logic)
        example="Taushiq Balamurugan")       # Example for documentation purposes      
    Department: Optional[str] = 'General'    # OPtional str (default 'General')
    Salary: float = Field(                   # Float must be >= 10000
        ...,
        ge=10000,                            # Greater than or equal to 
        alias='salary')                      # Different Field name
                              

input_data = {'id':1, 'Name':'Taushiq', 'salary':25000.00}
E = Employee(**input_data)

print(E)
