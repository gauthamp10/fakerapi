from flask import Flask, jsonify, request
from flask import render_template
from engine import *
import json
import gunicorn

@app.route("/")
def home():
    return render_template('index.html')
    
if __name__ ==  '__main__':
    app.run(host='0.0.0.0',debug=True)