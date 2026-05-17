from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = FastAPI(title="SLO Platform Demo App")

# Metrics
REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total request count",
    ["method", "endpoint", "status"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"],
    buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5]
)

@app.get("/health")
def health():
    REQUEST_COUNT.labels(method="GET", endpoint="/health", status="200").inc()
    return {"status": "healthy"}

@app.get("/api/data")
def get_data():
    start = time.time()
    
    # Simulate occasional errors (5% error rate)
    if random.random() < 0.05:
        REQUEST_COUNT.labels(method="GET", endpoint="/api/data", status="500").inc()
        REQUEST_LATENCY.labels(endpoint="/api/data").observe(time.time() - start)
        return Response(status_code=500, content="Internal Server Error")
    
    # Simulate latency (10-300ms)
    time.sleep(random.uniform(0.01, 0.3))
    
    REQUEST_COUNT.labels(method="GET", endpoint="/api/data", status="200").inc()
    REQUEST_LATENCY.labels(endpoint="/api/data").observe(time.time() - start)
    return {"data": "success", "timestamp": time.time()}

@app.get("/api/slow")
def slow_endpoint():
    start = time.time()
    
    # Simulate slow responses (500ms-2s)
    time.sleep(random.uniform(0.5, 2.0))
    
    REQUEST_COUNT.labels(method="GET", endpoint="/api/slow", status="200").inc()
    REQUEST_LATENCY.labels(endpoint="/api/slow").observe(time.time() - start)
    return {"data": "slow response", "timestamp": time.time()}

@app.get("/api/error")
def error_endpoint():
    # Always errors - for testing burn rate alerts
    REQUEST_COUNT.labels(method="GET", endpoint="/api/error", status="500").inc()
    return Response(status_code=500, content="Simulated Error")

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)