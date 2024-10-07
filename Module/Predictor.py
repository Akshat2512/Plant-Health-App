
import numpy as np

import requests
import json
import math, array
from io import BytesIO
import base64
import onnxruntime as ort
# from PIL import Image

class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Background___without_leaves', 'Blueberry___healthy', 'Cherry___healthy', 'Cherry___Powdery_mildew', 'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Corn___Common_rust', 'Corn___healthy', 'Corn___Northern_Leaf_Blight', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper_bell___Bacterial_spot', 'Pepper_bell___healthy', 'Potato___Early_blight', 'Potato___healthy', 'Potato___Late_blight', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___healthy', 'Strawberry___Leaf_scorch', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus']

img_height = 256
img_width = 256

def softmax(x):
    # e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    # return e_x / np.sum(e_x, axis=1, keepdims=True)

    max_vals = [max(row) for row in x]
    
    # Calculate the exponentials and subtract the max value
    e_x = [[math.exp(val - max_val) for val in row] for row, max_val in zip(x, max_vals)]
    
    # Calculate the sum of exponentials for each row
    sum_e_x = [sum(row) for row in e_x]
    
    # Normalize the exponentials
    softmax_result = [[val / sum_val for val in row] for row, sum_val in zip(e_x, sum_e_x)]

    return softmax_result

def onnx_model(dataURL):
    

    try:

        base64_content = dataURL.split(",")[1]
        # image_data = base64.b64decode(base64_content)
        # img = BytesIO(image_data)

        # img = Image.open(BytesIO(image_data)).convert('RGB').resize((img_height, img_width))
        data =  {
            'file' : base64_content
        }
        json_data = json.dumps(data)

        headers = {
            'Content-Type': 'application/json'
        }

        api_url = 'https://image-processing-zeta.vercel.app/process_image'
    
        # # Make the post request
        response = requests.post(api_url, data = json_data, headers=headers)
        # print(response.content)
        # # Check if the request was successful
        content = {}
        if response.status_code == 200:
           content = json.loads(response.content)  # Parse the JSON data
        else:
            return "error", response.status_code

        
        img_pixel_vals = content
    
        img_array = np.array(img_pixel_vals, dtype=np.float32)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array.reshape(1, 256, 256, 3)
        # print(img_array.shape)
        # img_data = list(img.getdata())
     
        # img_array = []
        # for y in range(img_height):
        #     row = []
        #     for x in range(img_width):
        #         pixel = img_data[y * img_width + x]
        #         row.append([float(channel) for channel in pixel])
        #     img_array.append(row)
        
        # img_array = [img_array]


        session = ort.InferenceSession("Model/model.onnx")        
        input_details = session.get_inputs()[0].name
        print(session.get_inputs()[0])
        predictions = session.run(None, {input_details: img_array})
       
        score = softmax(predictions[0])[0]
    
        a=class_names[score.index(max(score))]
        b=round(100 * max(score),2)

        # a = class_names[np.argmax(score)]
        # b=round(100 * np.max(score),2)
        data=a.split('___')
        b=str(b)
        
        jsn = {'Species': data[0], 'Health Status': data[1], 'Confidence': b}
        jsn_string = json.dumps(jsn)
        return jsn_string
    
    except Exception as e:
            print(e)

