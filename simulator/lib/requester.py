from prometheus_client import Counter, Histogram, start_http_server
import requests, os, time
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type, RetryError

start_http_server(8000)
load_dotenv()
API_ENDPOINT = os.getenv("API_ENDPOINT", "http://localhost:5000")

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of requests sent by the caller",
    ["method", "endpoint", "status"]
)
REQUEST_LATENCY = Histogram(
    "response_latency_seconds",
    "Latency of HTTP requests",
    ["method", "endpoint"]
)

def log_retry(retry_state):
    attempt_number = retry_state.attempt_number
    total_attempts = retry_state.kwargs.get('retries', 5)
    print(f"Attempt {attempt_number}/{total_attempts} failed for {retry_state.args[0]}: {retry_state.outcome.exception()}")

@retry(
    stop=stop_after_attempt(10),
    wait=wait_exponential(multiplier=5, min=1, max=60),
    retry=retry_if_exception_type(requests.exceptions.RequestException)
)
def sendRequest(endpoint):
    url = f"{API_ENDPOINT}{endpoint}"
    response = requests.post(url, timeout=20)
    
    REQUEST_COUNT.labels(
        method="POST",
        endpoint=endpoint,
        status=response.status_code
    ).inc()
    
    print(f"Requested {endpoint}, Status Code: {response.status_code}")

def safeSendRequest(endpoint, retries=5):
    try:
        start_time = time.time()
        sendRequest(endpoint)
        latency = time.time() - start_time
        REQUEST_LATENCY.labels(method="GET", endpoint="/sendRequest").observe(latency)    
    except RetryError as retry_error:
        REQUEST_COUNT.labels(
            method="POST",
            endpoint=endpoint,
            status="error"
        ).inc()

        print(f"Error: Max retries reached for {endpoint}. Giving up.")
        print(f"Final failure: {retry_error.last_attempt.exception()}")

def sendRequests(endpoint, count):
    with ThreadPoolExecutor(max_workers=count) as executor:
        futures = [executor.submit(safeSendRequest, endpoint) for _ in range(count)]
        for future in futures:
            future.result()
