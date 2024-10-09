import subprocess,json
from flask import Flask, render_template, request, redirect, Response, send_file
from Module.Predictor import onnx_model
import os
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    req_data = request.json
    data = req_data['img']
    response = onnx_model(data)
    return Response(response, mimetype='application/json')


@app.route('/download_model')
def image_proccessing():

    db_info = {
        "url" : 'https://ehtjvxl2iogyvqay.public.blob.vercel-storage.com/Model/model-3FP9R2vIqjWBfFotRI1ApeiQriTPhf.onnx',
    }
    
    print(os.listdir('/tmp'))
    if 'Model' not in os.listdir('/tmp'):

            response = requests.get(db_info['url'])
            if response.status_code == 200:
              os.makedirs('/tmp/Model', exist_ok=True)
              with open('/tmp/Model/model.onnx', 'wb') as file:
                file.write(response.content)

              return "File succesfully has been created<br><br>" + os.listdir('/tmp')
            else:
              return 'File saved Failed'
    else:    
      return "File already present!<br><br>" + os.listdir('/tmp')
    
# image_proccessing()  

# if __name__ == "__main__":
#     app.run(debug=True)