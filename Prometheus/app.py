from flask import Flask, jsonify
import os
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a counter for the number of requests
REQUEST_COUNT = Counter('python_web_app_requests_total', 'Total number of requests to the web application')

@app.route('/message', methods=['GET'])
def get_message():
    REQUEST_COUNT.inc()  # Increment the counter by 1
    message = os.getenv('MESSAGE', 'Hello, World!')
    return jsonify({"message": message})

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)