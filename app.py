from flask import Flask, request
from flask_cors import CORS
from chatbot_engine import get_response

app = Flask(__name__)
CORS(app)

@app.route("/get")
def chatbot_reply():
    msg = request.args.get("msg")
    if not msg:
        return "No message provided", 400
    return get_response(msg)

if __name__ == "__main__":
    app.run(debug=True)
