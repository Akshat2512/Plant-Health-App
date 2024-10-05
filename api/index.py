import subprocess,json
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/greet', methods=['POST'])
def index():
    return "hello_world"