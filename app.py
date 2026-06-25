import json
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)


def load_data():
    with open(os.path.join(os.path.dirname(__file__), "data.json")) as f:
        return json.load(f)


@app.route("/")
def dashboard():
    data = load_data()
    return render_template("index.html", data=data)


@app.route("/api/data")
def api_data():
    return jsonify(load_data())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
