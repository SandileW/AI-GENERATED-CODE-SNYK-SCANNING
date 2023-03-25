from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

def file_is_safe_type(file) -> bool:
    return True

#save uploaded files to the folder ./uploads
# if they are safe and if they are less than 2MB
@app.route('/file/upload')
# def upload_file():
#     f = request.files['f']
#-tabnine next line-


def upload_file():
    f = request.files['f']
    if file_is_safe_type(f) and f.filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg']:
        filename = f.filename
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
    else:
        return redirect(url_for('upload_file'))
        


