from flask import Flask, request, render_template, redirect, flash, session, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "24rjk24kj3"

@app.route("/")
def default_route():
    """default route"""

    return render_template("index.html")