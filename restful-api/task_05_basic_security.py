#!/usr/bin/python3
"""Module for API security and Authentication Techniques"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_jwt_extended import jwt_required, JWTManager, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "your-secret"
jwt = JWTManager(app)

users = {
        "john": {"username": "john", "password": generate_password_hash("hello"), "role": "user"},
        "jane": {"username": "jane", "password": generate_password_hash("bye"), "role": "admin"}
        }

tokens = {
        "abc123token": "john",
        "123abctoken": "jane"
        }

@auth.verify_password
def verify_password(username, password):
   if username in users and check_password_hash(users[username]["password"], password):
       return username
   return None

@app.route("/basic-protected")
@auth.login_required
def basic_protected():  
    return "Basic Auth: Access Granted"

@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()

    username = data["username"]
    password = data["password"]

    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def is_admin():
    username = get_jwt_identity()
    if users[username]["role"] == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Access Denied"}), 403

if __name__ == "__main__":
    app.run()
