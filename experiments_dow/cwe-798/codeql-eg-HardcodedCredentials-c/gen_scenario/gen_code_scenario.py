from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#def get_db_connection():
#-tabnine next line-

    db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='tabnine')
    cursor = db.cursor()
    return db, cursor


