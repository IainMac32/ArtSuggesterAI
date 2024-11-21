# flask backend for image uploading and retrieving
# aiden, johann

from flask import Flask, request, jsonify, send_from_directory, abort, send_file
import os
import zipfile
from flask_cors import CORS

app = Flask(__name__)

##Enable CORS ffor all routes
CORS(app)

# find/create upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# set the folder where files (images) will be uploaded to
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# root route for backend page
@app.route("/")
def main():
    return {"message": "Welcome to the file upload server!"}

# file upload route for backend
@app.route('/uploadFile', methods=['POST'])
def upload_file():
    # ensure the request has a file attached
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    # get the file name
    file = request.files['file']

    # no empty name files
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # save the file to the directory
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200

images_dir = app.config["SUGGESTED_IMAGES"] = "returnImages"
@app.route('/suggestedImages/<int:id>', methods=['GET'])
def get_images(id):
    print(images_dir)
    image_array = os.listdir(images_dir)
    image_to_send = image_array[id] 

    if image_to_send == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(images_dir, image_array[id])
    return send_file(file_path)

# run program
if __name__ == "__main__":
    app.run(debug=True)