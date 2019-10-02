from flask import Flask, jsonify, request, render_template, redirect
import store

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "hello world!"


@app.route("/api", methods=["GET"])
def get_all_data():
    all_data = store.get_all_data()
    return jsonify(all_data)


if __name__ == "__main__":
    app.run()
