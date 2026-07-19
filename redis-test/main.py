from fastapi import FastAPI
import redis
import time
import json
import random
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tasks import send_email

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

class Generate_OTP(BaseModel):
    email:str

class OTP(Generate_OTP):
    my_otp: int

@app.get("/")
def get_user():
    curr_count = r.incr("user:limit")
    if curr_count == 1:
        r.expire("user:limit", 10)
    
    if curr_count > 10:
        return {"message":"Wait for few seconds"}
        
    if r.get("user:data"):
        return json.loads(r.get("user:data"))
    else:
        time.sleep(2)
        user = {"name":"Vansh", "email":"vansh@gmail.com","age":23}
        r.set("user:data", json.dumps(user), ex=60)
        return user
    
@app.post('/generate_otp')
def generate_otp(generate_body:Generate_OTP):
    otp = random.randint(100000, 999999)
    r.set(f"email:{generate_body.email}", otp, ex=30)
    return {"otp":otp}

@app.post('/verify_otp')
def verify_otp(otp_body:OTP):
    otp = int(r.get(f"email:{otp_body.email}"))

    if otp is None:
        return {"message":"OTP not found or Expired : Please Regenerate"}
    
    if otp != otp_body.my_otp:
        return {"message":"Incorrect OTP"}
    
    return {"message":"OTP Verified"}

@app.post('/login')
async def login(user:Generate_OTP):
    result = send_email.delay(user.email)
    print(result)
    return {
        "message":"User Logged in",
        "email":user.email
    }