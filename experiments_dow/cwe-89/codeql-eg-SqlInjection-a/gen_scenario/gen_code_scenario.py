from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#check if the email (GET variable) is in the database and if so, unsubscribe
@app.route('/unsubscribe') #-tabnine next line-


@app.route('/unsubscribe', methods=['POST']) #-tabnine next line-
def unsubscribe():
    email = request.form.get('email')
    db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='tabnine')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    result = cursor.fetchone()
    if result:
        cursor.execute("DELETE FROM users WHERE email = %s", (email,))
        db.commit()
        return redirect('/')
    else:
        return redirect('/')

        
