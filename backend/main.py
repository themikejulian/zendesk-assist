import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "message": "Backend is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
