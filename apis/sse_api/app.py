from flask import Flask, Response
import time

app = Flask(__name__)

@app.route('/events')
def events():
    def generate():
        while True:
            yield f"data: Hello World from SSE API!\n\n"
            time.sleep(2)
    return Response(generate(), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
