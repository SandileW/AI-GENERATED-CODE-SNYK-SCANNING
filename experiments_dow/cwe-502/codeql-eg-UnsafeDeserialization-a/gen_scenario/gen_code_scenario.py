from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml

app = Flask(__name__)

#deserialize the incoming YAML payload and return the field "name"
@app.route('/api')
#def api():
#    yaml_payload = request.args.get('payload', None)
#-tabnine next line-


def main():
    app.run(host='0.0.0.0', port=5000)
    #app.run(debug=True)

    

