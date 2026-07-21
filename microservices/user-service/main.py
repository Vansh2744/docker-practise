from fastapi import FastAPI

app = FastAPI(title="User Service")

@app.get("/")
def read_root():
    return {"service": "user-service"}

@app.post("/login")
def login():
    return {"message":"User Logged in successfully", "email":"vansh@gmail.com"}