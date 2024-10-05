# import subprocess,json
from flask import Flask, render_template, request, redirect
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "hello"

@app.route('/greet', methods=['GET'])
def index():
    return "hello_world"