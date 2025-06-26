from fastapi import FastAPI

app = FastAPI()

@app.get("/")     # Decorator to define the route endpoint - instance of FastAPI - Here "/" is the base path
def index():
    return {"Data": {"Name": "Taushiq"}}

# Here get is the operation type (GET request) - @app is the path operation decorator
@app.get("/about") #Here "/about" is the about path
def about():
    return {"Data": "This is the about page"}

# Blog system
@app.get("/blog/{id}")   # Dynamic routing with path parameter
def show(id):            # Send the id as a path parameter
    return {"data": id}

