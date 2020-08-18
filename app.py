from flask import (
    Flask,
    request,
    render_template,
    session,
    flash,
    url_for,
    redirect,
    jsonify,
)

import json
import databaseFunctions
import re
import requests
import riveBot

app = Flask(__name__)


global objectUser
logged_in = False


@app.route("/")
def hello_world():
    return render_template("login.html")


@app.route("/login")
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = databaseFunctions.db_connect()
        user = databaseFunctions.get_user(conn, username, password)
        response = {}
        if user:
            session["logged_in"] = True
            response["status"] = "Success"
            response["data"] = user
            global objectUser
            objectUser = user
            global logged_in
            logged_in = True
            return render_template("index.html")
        else:
            response["status"] = "Failed"
            response["response"] = "Wrong Password"
            return jsonify(response), 400
    else:
        response = {}
        response["status"] = "Failed"
        response["response"] = "Method not allowed"

        return jsonify(response), 400


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/registration", methods=["POST"])
def registration():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = databaseFunctions.db_connect()
        user = databaseFunctions.check_user(conn, username)
        response = {}
        if user:
            response["status"] = "Failed"
            response[
                "response"
            ] = "user with same name exists please try a new username"
            return redirect(url_for("register"))
        else:
            databaseFunctions.add_user(conn, request.form)
            response["status"] = "Success"
            response["response"] = "registered correctly you can now login"
            return redirect(url_for("login"))
    else:
        response = {}
        response["status"] = "Failed"
        response["response"] = "Method not allowed"

        return jsonify(response), 400


@app.route("/chat", methods=["POST"])
def chat():
    if request.method == "POST":

        json_data = request.get_json()

        state, reply = riveBot.chat("1", json_data["message"])
        if state == 0:
            return json.loads(r"" + reply)
        else:
            return jsonify({"message": "something went wrong bot did not reply"})


if __name__ == "__main__":
    app.run(debug=True)

