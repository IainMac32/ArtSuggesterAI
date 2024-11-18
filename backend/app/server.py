# flask backend for image uploading and retrieving
# aiden, johann

from flask import Flask, request, jsonify
import os

app = Flask(__name__)

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

# run program
if __name__ == "__main__":
    app.run(debug=True)