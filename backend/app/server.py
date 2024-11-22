from flask import Flask, request, jsonify, send_file, abort
import os
from flask_cors import CORS
from processUserImage import processUserImage
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from collections import Counter
from scipy.spatial import cKDTree
from PIL import Image
from sklearn.cluster import KMeans
from skimage.color import rgb2lab, deltaE_cie76
from similaritySearch import SimilaritySearch
from scipy.spatial.distance import cdist



app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Find/create upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Set the folder where files (images) will be uploaded to
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Root route for backend page
@app.route("/")
def main():
    return {"message": "Welcome to the file upload server!"}

# File upload route for backend
@app.route('/uploadFile', methods=['POST'])
def upload_file():
    # Ensure the request has a file attached
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    # Get the file name
    file = request.files['file']

    # No empty name files
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file to the directory
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_path)

    processUserImage(file_path)
    

    return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200

# Directory for suggested images
SUGGESTED_IMAGES_DIR = 'returnImages'
if not os.path.exists(SUGGESTED_IMAGES_DIR):
    os.makedirs(SUGGESTED_IMAGES_DIR)

@app.route('/suggestedImages/<int:id>', methods=['GET'])
def get_images(id):
    try:
        # Get the list of images in the directory
        image_array = sorted(os.listdir(SUGGESTED_IMAGES_DIR))

        # Check if the requested index exists
        if id < 0 or id >= len(image_array):
            return jsonify({"error": "Image ID out of range"}), 404

        # Construct the file path
        image_to_send = image_array[id]
        file_path = os.path.join(SUGGESTED_IMAGES_DIR, image_to_send)

        file_path = os.path.join(SUGGESTED_IMAGES_DIR, image_to_send)
        print("Trying to serve file:", file_path)


        # Serve the image file
        return send_file(file_path)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run program
if __name__ == "__main__":
    app.run(debug=True)
