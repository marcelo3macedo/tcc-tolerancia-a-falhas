import requests, os
from dotenv import load_dotenv

load_dotenv()
API_ENDPOINT = os.getenv("API_ENDPOINT", "http://localhost:5000")

def sendRequests(endpoint, count):
    url = f"{API_ENDPOINT}{endpoint}"
    for _ in range(count):
        try:
            response = requests.post(url)
            print(f"Requested {endpoint}, Status Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error requesting {endpoint}: {e}")