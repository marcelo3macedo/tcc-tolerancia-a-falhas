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

@app.route("/message/cpu", methods=["POST"])
def message():
    simulateCpuLoad(duration=5)
    
    return jsonify({
        "status": "ok",
        "message": "Message using CPU received.",
    })

@app.route("/message/memory", methods=["POST"])
def message_status():
    simulateMemoryLoad(size_mb=1, duration=1)

    return jsonify({
        "status": "ok",
        "message": "Message using Memory received."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
