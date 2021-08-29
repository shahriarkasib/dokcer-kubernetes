from flask import Flask,jsonify
import time

app = Flask(__name__)


@app.route("/")

def hello_world():
    return jsonify({"Time To Call": time.time()})


if __name__ == "__main__":
    app.run()