from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#save the uploaded pdf file to ./uploads directory
@app.route('/pdf/upload')
#def upload_pdf():
#    p = request.files['pdf']
#-tabnine next line-


def upload_pdf():
    p = request.files['pdf']
    p.save(os.path.join(app.config['UPLOAD_FOLDER'], p.filename))
    return redirect(url_for('uploaded_pdf', filename=p.filename))

    




