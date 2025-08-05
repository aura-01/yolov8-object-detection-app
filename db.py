# db.py
from pymongo import MongoClient
from PIL import Image
import io
import datetime

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["object_detection"]
collection = db["detections"]

def save_detection(image_np_array, detections, filename):
    img = Image.fromarray(image_np_array)
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')

    document = {
        "filename": filename,
        "timestamp": datetime.datetime.utcnow(),
        "detections": detections,
        "image": img_byte_arr.getvalue()
    }
    collection.insert_one(document)
