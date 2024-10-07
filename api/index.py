import subprocess,json
from flask import Flask, render_template, request, redirect, Response, send_file
from Module.Predictor import onnx_model
from Module.process import process_image
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    req_data = request.json
    data = req_data['img']
    response = onnx_model(data)
    return Response(response, mimetype='application/json')

# @app.route('/process_image', methods=['POST'])
# def image_proccessing():
#     data = request.json['file']
#     response = process_image(data)
#     response = json.dumps(response)
#     # print(response)
#     return Response(response, mimetype='application/json')

# if __name__ == "__main__":
#     app.run(debug=True)