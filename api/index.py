import subprocess,json
from flask import Flask, render_template, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "hello"

@app.route('/send', methods=['POST'])
def  greet():
    response = request.json
    return "hello_world"
