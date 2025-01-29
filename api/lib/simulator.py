import time

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
        response = requests.get("https://httpbin.org/get", timeout=5)
        print("Network Request Successful:", response.status_code)
        return response.status_code
    except requests.RequestException as e:
        print("Network Request Failed:", e)
        return None