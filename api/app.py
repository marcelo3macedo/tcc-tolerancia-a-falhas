from flask import Flask, jsonify
from lib.simulator import simulateCpuLoad, simulateMemoryLoad
import multiprocessing
import time
import os

app = Flask(__name__)

@app.route("/message", methods=["POST"])
def message():
    simulateCpuLoad(duration=0.5)
    simulateMemoryLoad(size_mb=5, duration=0.1)

    return jsonify({
        "status": "ok",
        "message": "Message received.",
    })

@app.route("/message/status", methods=["POST"])
def message_status():
    simulateCpuLoad(duration=0.2)
    simulateMemoryLoad(size_mb=5, duration=0.1)

    return jsonify({
        "status": "ok",
        "message": "Status received."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
