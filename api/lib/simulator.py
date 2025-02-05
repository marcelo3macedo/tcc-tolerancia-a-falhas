import time, requests
from prometheus_client import Counter, start_http_server

start_http_server(8001)

REQUEST_COUNT = Counter(
    "network_requests_total",
    "Total number of requests sent by the caller in network",
    ["method", "endpoint", "status"]
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
    try:
        response = requests.get("http://receiver:5001/process", timeout=5)
        REQUEST_COUNT.labels(
            method="GET",
            endpoint="/process",
            status=response.status_code
        ).inc()
        print("Network Request Successful:", response.status_code)
        return response.status_code
    except requests.RequestException as e:
        REQUEST_COUNT.labels(
            method="GET",
            endpoint="/process",
            status="error"
        ).inc()
        print("Network Request Failed:", e)
        return None