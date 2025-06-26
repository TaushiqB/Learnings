from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Data": {"Name": "Taushiq"}}

@app.get("/about")
def about():
    return {"Data": "This is the about page"}