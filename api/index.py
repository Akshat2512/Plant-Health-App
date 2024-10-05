import subprocess,json
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
    return "hello"

@app.route('/greet', methods=['GET'])
def index():
    return "hello_world"