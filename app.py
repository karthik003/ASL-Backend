from flask import Flask, request, jsonify
import os
import tempfile
import base64
from main2 import *
app = Flask(__name__)

PERMANENT_STORAGE_FOLDER = '/Users/karthik003/Desktop/External-Projects/ASL/ASL-Backend/audios'
IMAGE_STORAGE_FOLDER = '/Users/karthik003/Desktop/External-Projects/ASL/ASL-Backend/responses'  # Update this path to where you want to save images

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    permanent_file_path = os.path.join(PERMANENT_STORAGE_FOLDER, file.filename)
    file.save(permanent_file_path)

    try:
        recognized_images = func(permanent_file_path)
        save_images(recognized_images)
        return jsonify({"recognized_images": recognized_images}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

def save_images(image_data_list):
    for index, image_data in enumerate(image_data_list):
        if image_data.get('type') == 'image' and image_data.get('data'):
            image_base64 = image_data['data']
            file_path = os.path.join(IMAGE_STORAGE_FOLDER, f'image_{index}.jpg')
            save_image_from_base64(image_base64, file_path)

def save_image_from_base64(data, file_path):
    with open(file_path, "wb") as file:
        file.write(base64.b64decode(data))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
