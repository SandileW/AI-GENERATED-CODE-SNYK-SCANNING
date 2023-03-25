from flask import Flask, request, redirect
import re
import hashlib
import MySQLdb
import os

app = Flask(__name__)

#register url
@app.route('/register', methods=['POST'])
def register():
   username = request.form['username']
   password = request.form['password']
   #hash the password
   salt = os.urandom(16)
#-tabnine next line-
   password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
   #insert into user table
   try:
      conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='tabnine')
      cur = conn.cursor()
      cur.execute("INSERT INTO user (username, password_hash) VALUES (%s, %s)", (username, password_hash))
      conn.commit()
      cur.close()
      conn.close()
   except MySQLdb.Error as e:
      print(e)
   return redirect('/')
   