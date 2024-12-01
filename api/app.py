from flask import Flask, jsonify, request
from lib.simulator import simulateCpuLoad, simulateMemoryLoad
from prometheus_client import Counter, start_http_server
import multiprocessing
import os, time

app = Flask(__name__)

REQUEST_COUNT = Counter(
    'http_requests_total', 
    'Total HTTP requests', 
    ['method', 'endpoint', 'status']
)

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        status=response.status_code
    ).inc()
    return response

@app.route("/message", methods=["POST"])
def message():
    simulateCpuLoad(duration=1)
    simulateMemoryLoad(size_mb=10, duration=1)

    return jsonify({
        "status": "ok",
        "message": "Message received.",
    })

@app.route("/message/status", methods=["POST"])
def message_status():
    simulateCpuLoad(duration=1)
    simulateMemoryLoad(size_mb=10, duration=1)

    return jsonify({
        "status": "ok",
        "message": "Status received."
    })

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
