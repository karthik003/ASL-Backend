from flask import Flask, request, jsonify
import os
import tempfile
import speech_recognition as sr
import string
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from main2 import *
app = Flask(__name__)


@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    print(file)

    # Save the received audio file to a temporary location
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, file.filename)
    file.save(temp_file_path)

    try:
        # Call the func() function with the path to the saved audio file
        recognized_images = func(temp_file_path)

        # You can perform any additional processing with the recognized images or return them in the response.
        return jsonify({"recognized_images": recognized_images}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
    finally:
        # Delete the temporary audio file after processing
        os.remove(temp_file_path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
