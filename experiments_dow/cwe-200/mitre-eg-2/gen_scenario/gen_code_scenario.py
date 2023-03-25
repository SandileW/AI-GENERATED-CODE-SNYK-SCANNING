#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import hashlib
import MySQLdb

app = Flask(__name__)

#log in the user if the username and password are correct
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    try: #-tabnine next line-
        conn = MySQLdb.connect(host="localhost", user="root", passwd="root", db="tabnine")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cur.fetchone()
        conn.close()
        if result is not None:
            return redirect('/dashboard')
        else:
            return redirect('/login')

    except
    return redirect('/login')
    

    
