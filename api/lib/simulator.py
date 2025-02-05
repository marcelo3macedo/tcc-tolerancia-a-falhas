import time, requests, os
from prometheus_client import Counter, Histogram, start_http_server
import logging

start_http_server(8001)
logging.basicConfig(level=logging.INFO)

REQUEST_COUNT = Counter(
    "network_requests_total",
    "Total number of requests sent by the caller in network",
    ["method", "endpoint", "status"]
)
REQUEST_LATENCY = Histogram(
    "network_request_latency_seconds",
    "Latency of HTTP requests",
    ["method", "endpoint"]
)

def simulateCpuLoad(duration=0.5):
    """Simulates CPU load for a specified duration."""
    start = time.time()
    while time.time() - start < duration:
        _ = sum(i * i for i in range(1000))

def simulateMemoryLoad(size_mb=10, duration=1):
    """Simulates memory load by allocating a block of memory."""
    data = bytearray(size_mb * 1024 * 1024)
    time.sleep(duration)
    del data

def performNetworkRequest():
    """Performs a network request and waits for completion."""
    start_time = time.time()
    endpoint = os.getenv("RECEIVER_ENDPOINT", "http://receiver:5001/process")

    try:
        response = requests.get(endpoint, timeout=5)
        latency = time.time() - start_time
        REQUEST_LATENCY.labels(method="GET", endpoint="/process").observe(latency)
        REQUEST_COUNT.labels(
            method="GET",
            endpoint="/process",
            status=response.status_code
        ).inc()
        logging.info("Network Request Successful: %s", response.status_code)
        return response.status_code
    except requests.RequestException as e:
        REQUEST_COUNT.labels(
            method="GET",
            endpoint="/process",
            status="error"
        ).inc()
        logging.info("Network Request error: %s")
        return None