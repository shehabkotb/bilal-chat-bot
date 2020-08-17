import json
from flask import Flask, request, render_template, session,flash,url_for,redirect
import jsonify
import databaseFunctions
import re
from importlib import reload
import requests

app = Flask(__name__)
import ipdb
import riveBot
from flask import jsonify

global objectUser
logged_in = False


@app.route('/')
def hello_world():
    return render_template("login.html")


@app.route('/login')
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        conn = databaseFunctions.db_connect()
        user = databaseFunctions.get_user(conn, username, password)
        response = {}
        if user:
            session['logged_in'] = True
            response["status"] = "Success"
            response['data'] = user
            global objectUser
            objectUser = user
            global logged_in
            logged_in = True
            return render_template("index.html")
        else:
            response["status"] = "Failed"
            response['response'] = "Wrong Password"
            return jsonify(response), 400
    else:
        response = {}
        response["status"] = "Failed"
        response['response'] = "Method not allowed"

        return jsonify(response), 400
    
@app.route('/register')
def register():
    return render_template('register.html')
