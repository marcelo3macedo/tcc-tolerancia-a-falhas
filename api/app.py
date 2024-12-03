from flask import Flask, jsonify, request
from lib.simulator import simulateCpuLoad, simulateMemoryLoad
import multiprocessing
import os, time

app = Flask(__name__)

@app.before_request
def before_request():
    request.start_time = time.time()

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "message": "Service is running."
    }), 200    

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
    app.run(host="0.0.0.0", port=5000)
