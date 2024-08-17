from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/message', methods=['GET'])
def get_message():
    message = os.getenv('MESSAGE', 'Hello, World!')
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)