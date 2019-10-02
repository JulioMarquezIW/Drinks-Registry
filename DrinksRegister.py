from flask import Flask, jsonify, request, render_template, redirect
import store

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_active_drinks():
    return "hello world!"

if __name__ == "__main__":
    app.run()
