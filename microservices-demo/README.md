# FastAPI Microservices - Minimal Example

Three independent services (`user-service`, `order-service`, `product-service`), each
with a single `GET /` route that returns its own name, plus a `gateway` that proxies
requests to them.

## Structure
```
microservices-demo/
├── user-service/main.py
├── order-service/main.py
├── product-service/main.py
├── gateway/main.py
├── docker-compose.yml
└── requirements.txt
```

## Option 1: Run locally (no Docker)

Install dependencies once:
```bash
pip install -r requirements.txt
```

Open 4 terminals and run each service on its own port:
```bash
uvicorn main:app --app-dir user-service --port 8001
uvicorn main:app --app-dir order-service --port 8002
uvicorn main:app --app-dir product-service --port 8003
uvicorn main:app --app-dir gateway --port 8000
```

Test:
```bash
curl localhost:8001/          # {"service": "user-service"}
curl localhost:8002/          # {"service": "order-service"}
curl localhost:8003/          # {"service": "product-service"}

curl localhost:8000/users     # via gateway -> user-service
curl localhost:8000/orders    # via gateway -> order-service
curl localhost:8000/products  # via gateway -> product-service
```

## Option 2: Run with Docker Compose

```bash
docker compose up --build
```

Same endpoints as above, gateway on port 8000, individual services exposed on
8001/8002/8003 for direct testing.

## How it works

- Each service is a **fully independent FastAPI app** (own `main.py`, own Dockerfile,
  own container). In a real system each would also have its own database and repo.
- The **gateway** is just another FastAPI app that uses `httpx` to forward requests
  to the right service based on the URL path, and returns the result. This is the
  single entry point clients would talk to.
- Service locations are read from environment variables (`USER_SERVICE_URL`, etc.),
  defaulting to `localhost` ports for local dev and swapped to Docker service names
  (`http://user-service:8000`) in `docker-compose.yml`. This is the core idea behind
  service discovery — the gateway doesn't hardcode where services live.

## Next steps to make this production-like

- Give each service its own database (see the earlier full example)
- Add a message broker (RabbitMQ/Kafka) for async/event-driven communication
- Add retries/circuit breakers around the gateway's HTTP calls
- Add centralized auth (JWT validated at the gateway)
- Add distributed tracing (OpenTelemetry) so a request can be traced across services
