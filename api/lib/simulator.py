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