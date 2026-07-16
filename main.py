from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def user():
    return {"message":"Everthing is working fine"}