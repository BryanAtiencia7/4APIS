from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello World from REST API!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
