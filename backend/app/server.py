from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ensure the upload folder exists
UPLOAD_FOLDER = 'uploads'  # You can modify this path as needed
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Set the folder where files will be stored
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def main():
    return {"message": "Welcome to the file upload server!"}

@app.route('/uploadFile', methods=['POST'])
def upload_file():
    # Check if the file part is in the request
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file to the server
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200

if __name__ == "__main__":
    app.run(debug=True)