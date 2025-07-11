from flask import Flask, render_template, request
from chatbot_engine import get_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def chatbot_reply():
    user_msg = request.args.get("msg")
    return get_response(user_msg)

if __name__ == "__main__":
    app.run(debug=True)
