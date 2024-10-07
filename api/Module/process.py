from PIL import Image
from io import BytesIO
import base64

img_height = 256
img_width = 256
def process_image(dataURL):
    
        image_data = base64.b64decode(dataURL)
        img = list(Image.open(BytesIO(image_data)).convert('RGB').resize((img_height, img_width)).getdata())
        # img_io = BytesIO()
        # img.save(img_io, 'JPEG')
        # img_io.seek(0)
        return img