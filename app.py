#import required libraries
from flask import Flask, flash, jsonify, redirect, render_template, request, session

#start flask app
app = Flask(__name__)

#default route/path
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")