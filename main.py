from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

name = os.getenv("NAME")

app = FastAPI()

@app.get('/')
def user():
    return {"message":f"Everthing is working fine : {name}"}