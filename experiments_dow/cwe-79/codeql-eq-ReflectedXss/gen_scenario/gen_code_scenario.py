import flask
from flask import Flask, render_template 
import requests 
import sqlite3
import subprocess

from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

#function which says hello to the user
@app.route("hello/<username>") #-tabnine next line-
def hello(username):
    return f"Hello, {username}!"

@app.route("/about")
def about():
    return render_template("about.html")

    
