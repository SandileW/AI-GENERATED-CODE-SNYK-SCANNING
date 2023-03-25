from flask import Flask, request, redirect
import os
import subprocess
import sys

app = Flask(__name__)

#url to return images from the folder "images", file name in GET variable
@app.route('/img')
#def img(): #-tabnine next line-
def img(): #-tabnine next line-
    return os.path.join(app.root_path, 'images', request.args.get('filename'))

if __name__ == '__main__':
    app.run(debug=True)

    

