import subprocess,json
from flask import Flask, render_template, request, redirect, Response
from api.Module.Predictor import onnx_model
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def greet():
    req_data = request.json
    data = req_data['img']
    response = onnx_model(data)
    return Response(response, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)