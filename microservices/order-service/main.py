from fastapi import FastAPI

app = FastAPI(title="Order Service")

@app.get("/")
def read_root():
    return {"service": "order-service"}

@app.post("/order-placed")
def place_order():
    return {"message":"Order Placed Successfully", "address":"VPO Paprola teh baijnath"}