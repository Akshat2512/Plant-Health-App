import subprocess,json
from flask import Flask, render_template, request, redirect
from Module.Predictor import prediction
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/process', methods=['POST'])
def greet():
    req = request.json
    data = req_data['img']
    response = tflite_model(data)
    return Response(response, mimetype='application/json')

