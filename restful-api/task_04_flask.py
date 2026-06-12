#!/usr/bin/python3
"""Module to develop simple API using Python with Flask"""
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def json_return():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])

@app.route("/add_user", methods=['POST'])
def add_user():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error":"Invalid JSON"}), 400
    if "username" not in data:
        return jsonify({"error":"Username is required"}), 400
    if data["username"] in users:
        return jsonify({"error":"Username already exists"}), 409
    users[data["username"]] = data
    return jsonify({"message":"User added", "user":data}), 201

if __name__ == "__main__": app.run()
