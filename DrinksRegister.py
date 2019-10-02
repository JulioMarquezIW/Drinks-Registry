from flask import Flask, jsonify, request, render_template, redirect, Response
import store

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "hello world!"


@app.route("/api", methods=["GET"])
def get_all_data():
    all_data = store.get_all_data()
    return jsonify(all_data)


@app.route("/api/drink", methods=["GET", "POST", "PUT", "DELETE"])
def add_new_drink():
    if request.method == 'GET':
        all_data = store.get_all_data()
        return jsonify(all_data)
    if request.method == 'POST':
        data = request.get_json() or {}
        store.add_new_drink(data['drink_name'], data['stock'])

        return Response(status=201)

    if request.method == 'PUT':
        data = request.get_json() or {}
        store.update_drink(data['drink_id'], data['drink_name'], data['stock'])

        return Response(status=201)

    if request.method == 'DELETE':
        data = request.get_json() or {}
        store.delete_drink(data['drink_id'])

        return Response(status=201)


@app.route("/api/drink/<int:id>", methods=["GET"])
def get_drink_by_id(id):
    if request.method == 'GET':
        all_data = store.get_all_data_by_id(id)
        return jsonify(all_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
