from flask import (
    Flask,
    request,
    render_template,
    g,
    session,
    flash,
    url_for,
    redirect,
    jsonify,
)

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from db import get_db

import db
import functools
import json
import re
import riveBot


app = Flask(__name__)
app.config.from_object("config")
db.init_app(app)

# decorator function
def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        user_id = session.get("user_id")

        if user_id is None:
            return redirect(url_for("login"))

        return view(**kwargs)

    return wrapped_view


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("index"))

        flash(error)

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register a new user.
    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif (
            db.execute("SELECT id FROM user WHERE username = ?", (username,)).fetchone()
            is not None
        ):
            error = "User {0} is already registered.".format(username)

        if error is None:
            # the name is available, store it in the database and go to
            # the login page
            db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
            return redirect(url_for("login"))

        flash(error)

    return render_template("register.html")


@app.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("login"))


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    if request.method == "POST":
        user_id = session.get("user_id")

        g.user = (
            get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        )

        json_data = request.get_json()

        state, reply = riveBot.chat(g.user["id"], json_data["message"])
        # ipdb.set_trace()
        if state == 0:
            return eval(reply.encode("unicode_escape"))
        else:
            return jsonify({"message": "something went wrong bot did not reply"})


@app.route("/settings", methods=["POST"])
def settings():

    if request.method == "POST":
        user_id = session.get("user_id")

        if user_id == None:
            return "unauthorized", 401

        surah_reciter = request.json["surah_reciter"]
        verse_reciter = request.json["verse_reciter"]

        db = get_db()
        db.execute(
            "UPDATE user SET surah_reciter = ?, verse_reciter = ? WHERE id = ?",
            (surah_reciter, verse_reciter, user_id),
        )
        db.commit()

        return "updated", 200


if __name__ == "__main__":
    app.run()

