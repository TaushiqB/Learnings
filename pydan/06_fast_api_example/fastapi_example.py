from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str

class Settings(BaseModel):
    app_name: str = "Fuck this life"
    admin_email: str = "I hate my life"

def get_settings():
    return Settings()  # Passed as an Instance 
 
@app.post('/signup')
def signup(user: UserSignup):
    return {'message': f'user {user.username} signed up successfully'}

@app.get('/settings')
def get_settings_endpoint(settings: Settings = Depends(get_settings)):
    return settings
# It is sent as a dependency injection