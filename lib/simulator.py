import time

def simulate_cpu_load(duration=0.5):
    """Simulates CPU load for a specified duration."""
    start = time.time()
    while time.time() - start < duration:
        _ = sum(i * i for i in range(1000))

def simulate_memory_load(size_mb=10, duration=1):
    """Simulates memory load by allocating a block of memory."""
    data = bytearray(size_mb * 1024 * 1024)
    time.sleep(duration)
    del data