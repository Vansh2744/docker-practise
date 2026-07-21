from fastapi import FastAPI

app = FastAPI(title="Product Service")

@app.get("/")
def read_root():
    return {"service": "product-service"}

@app.post("/check-product")
def check():
    return {"message":"This product checked"}