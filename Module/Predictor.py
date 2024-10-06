import onnxruntime as ort
import numpy as np
# # import tensorflow as tf
# import tflite_runtime.interpreter as tflite
from scipy.special import softmax
from PIL import Image
import json

from io import BytesIO
import base64


class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Background___without_leaves', 'Blueberry___healthy', 'Cherry___healthy', 'Cherry___Powdery_mildew', 'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Corn___Common_rust', 'Corn___healthy', 'Corn___Northern_Leaf_Blight', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper_bell___Bacterial_spot', 'Pepper_bell___healthy', 'Potato___Early_blight', 'Potato___healthy', 'Potato___Late_blight', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___healthy', 'Strawberry___Leaf_scorch', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus']

img_height = 256
img_width = 256

def onnx_model(dataURL):
    
    try:

        base64_data = dataURL.split(",")[1]
        image_data = base64.b64decode(base64_data)
        img = Image.open(BytesIO(image_data)).convert('RGB').resize((img_height, img_width))
  
        img_array = np.array(img, dtype=np.float32)
        img_array = np.expand_dims(img_array, axis=0)


        session = ort.InferenceSession("Model/model.onnx")        
        input_details = session.get_inputs()[0].name
        
        predictions = session.run(None, {input_details: img_array})
       
        score = softmax(predictions[0])

        a=class_names[np.argmax(score)]
        b=round(100 * np.max(score),2)
        
        data=a.split('___')
        b=str(b)
        
        jsn = {'Species': data[0], 'Health Status': data[1], 'Confidence': b}
        jsn_string = json.dumps(jsn)
        return jsn_string
    
    except Exception as e:
            print(e)

