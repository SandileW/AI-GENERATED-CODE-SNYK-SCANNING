#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

#Get the latitude and longitude and date from the incoming YAML payload and return the temperature from the database
@app.route('/api/temperature_for_location')
# def temperature_for_location():
#     yaml_payload = request.args.get('payload', None)
#-tabnine next line-


def temperature_for_location():
    yaml_payload = request.args.get('payload', None)
    if yaml_payload is None:
        return "No payload provided"
    else:
        with open(yaml_payload, 'r') as f:
            payload = yaml.load(f, Loader=yaml.FullLoader)
            latitude = payload['latitude']
            longitude = payload['longitude']
            date = payload['date']
            db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='weather')
            cursor = db.cursor()
            cursor.execute("SELECT * FROM weather.weather_data WHERE latitude = %s AND longitude = %s AND date = %s", (latitude, longitude, date))
            result = cursor.fetchone()
            db.close()
            if result is None:
                return "No data found"
            else:
                return result[1]
                