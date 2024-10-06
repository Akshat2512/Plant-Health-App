import subprocess,json
from flask import Flask, render_template, request, redirect, Response
from ..Module.Predictor import onnx_model


app = Flask(__name__)


@app.route('/process', methods=['POST'])
def greet():
    req_data = request.json
    data = req_data['img']
    print(data)
    response = onnx_model(data)
    return Response(response, mimetype='application/json')

