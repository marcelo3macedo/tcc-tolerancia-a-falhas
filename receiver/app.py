from flask import Flask, jsonify, request
import time

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "message": "Service is running."
    }), 200  

@app.route("/process", methods=["GET"])
def process_request():
    time.sleep(0.2)
    return jsonify({
        "status": "ok",
        "message": "Response after 200ms"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)