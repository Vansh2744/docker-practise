import os
from fastapi import FastAPI
import httpx

app = FastAPI(title="API Gateway")

SERVICE_MAP = {
    "users": os.getenv("USER_SERVICE_URL", "http://localhost:8001"),
    "orders": os.getenv("ORDER_SERVICE_URL", "http://localhost:8002"),
    "products": os.getenv("PRODUCT_SERVICE_URL", "http://localhost:8003"),
}

@app.get("/{service}")
async def proxy_get(service: str):
    if service not in SERVICE_MAP:
        return {"error": f"Unknown service '{service}'"}

    url = SERVICE_MAP[service]
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            return response.json()
        except httpx.RequestError:
            return {"error": f"{service} service is unavailable"}

@app.post("/{service}/{path}")
async def proxy_post(service: str, path: str):
    if service not in SERVICE_MAP:
        return {"error": f"Unknown service '{service}'"}

    url = f"{SERVICE_MAP[service]}/{path}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, timeout=5.0)
            return response.json()
        except httpx.RequestError:
            return {"error": f"{service} service is unavailable"}