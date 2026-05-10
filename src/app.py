import os
from flask import Flask, jsonify

app = Flask(__name__)

# Retrieve version from environment variable, default to '1.0.0'
VERSION = os.environ.get("APP_VERSION", "1.0.0")
VERSION = "2.0.0"

@app.route('/')
def home():
    return jsonify({
        "status": "running",
        "version": VERSION,
        "message": f"You are running version {VERSION} of the container."
    })

if __name__ == "__main__":
    # host='0.0.0.0' is required for Docker to expose the app
    app.run(host='0.0.0.0', port=5000)
