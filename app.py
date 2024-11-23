from flask import Flask, jsonify
from lib.simulator import simulate_cpu_load, simulate_memory_load
import multiprocessing
import time
import os

app = Flask(__name__)

@app.route("/message", methods=["POST"])
def message():
    simulate_cpu_load(duration=0.5)
    simulate_memory_load(size_mb=5, duration=0.1)

    return jsonify({
        "status": "ok",
        "message": "Message received.",
    })

@app.route("/message/status", methods=["POST"])
def message_status():
    simulate_cpu_load(duration=0.2)
    return jsonify({
        "status": "ok",
        "message": "Status received."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
