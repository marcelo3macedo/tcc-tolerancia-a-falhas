from prometheus_client import Counter, start_http_server
import requests, os
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor

start_http_server(8000)
load_dotenv()
API_ENDPOINT = os.getenv("API_ENDPOINT", "http://localhost:5000")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of requests sent by the caller",
    ["method", "endpoint", "status"]
)

def sendRequest(endpoint):
    url = f"{API_ENDPOINT}{endpoint}"
    try:
        response = requests.post(url)
        
        REQUEST_COUNT.labels(
            method="POST",
            endpoint=endpoint,
            status=response.status_code
        ).inc()
        
        print(f"Requested {endpoint}, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        REQUEST_COUNT.labels(
            method="POST",
            endpoint=endpoint,
            status="error"
        ).inc()

        print(f"Error requesting {endpoint}: {e}")

def sendRequests(endpoint, count):
    with ThreadPoolExecutor(max_workers=count) as executor:
        futures = [executor.submit(sendRequest, endpoint) for _ in range(count)]
        for future in futures:
            future.result()
