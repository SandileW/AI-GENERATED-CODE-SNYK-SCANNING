from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

#log in the user if the username and password are correct
@app.route('/login', methods=['POST'])
#def login():
#    username = request.form['username']
#    password = request.form['password']
#    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-tabnine next line-


#    cursor = db.cursor()


#    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))


#    db.commit()

