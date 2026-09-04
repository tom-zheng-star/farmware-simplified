from fastapi import FastAPI

app = FastAPI()

@app.get("/")   #When someone sends a GET request to the / path, call the function right below this line.
def read_root(): 
    return {"message": "Hello, Farmware backend is running."}