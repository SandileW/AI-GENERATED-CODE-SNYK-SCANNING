from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

@app.route('/buy_order', methods=['POST'])
# def buy_stock():
#     stock_name = request.form['stock_name']
#     stock_quantity = request.form['stock_quantity']
#     username = session['username']

#     #insert the buy order in the database
#     db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="db")
#-tabnine next line-


#     cursor = db.cursor()


#     sql = "INSERT INTO buy_order (stock_name, stock_quantity, username) VALUES (%s, %s, %s)"


#     cursor.execute(sql, (stock_name, stock_quantity, username))


#     db.commit()


#     cursor.close()


#     db.close()


#     return redirect('/')

