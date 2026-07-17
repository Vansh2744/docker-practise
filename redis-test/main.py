from fastapi import FastAPI
import redis
import time
import json

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

@app.get("/")
def get_user():
    if r.get("user:data"):
        return json.loads(r.get("user:data"))
    else:
        time.sleep(2)
        user = {"name":"Vansh", "email":"vansh@gmail.com","age":23}
        r.set("user:data", json.dumps(user))
        return user