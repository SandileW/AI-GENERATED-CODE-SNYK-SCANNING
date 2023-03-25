from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

#register url
@app.route('/register', methods=['POST'])
# def register():
#    username = request.form['username']
#    password = request.form['password']
#    #hash the password
#-tabnine next line-


def register():
    username = request.form['username']
    password = request.form['password']
    #hash the password
    hash_pass = hashlib.sha256(password.encode('utf-8')).hexdigest()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, hash_pass)
    try:
        db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='test')
        cursor = db.cursor()
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        return redirect('/login')
    except:
        return redirect('/register')