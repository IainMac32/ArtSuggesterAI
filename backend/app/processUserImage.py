import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import InputLayer

from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from PIL import Image
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Get the current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

uploads_dir = os.path.join(script_dir, "uploads")
file_path = os.path.join(uploads_dir, "uploadedImage.jpg")

# Check if the file exists
if os.path.exists(file_path):
    print(f"File found: {file_path}")
    # Do something with the file
else:
    print(f"File not found: {file_path}")
print('')

print("still good here")
print('')
if os.path.exists('models/detectMediumModel.keras'):
    print("Model file exists")
else:
    print("Model file not found")


print(f"TensorFlow version: {tf.__version__}")

# Load the trained model
model = load_model('models/detectMediumModel.keras')

print("loaded model")
print('')
print("Model input shape:", model.input_shape)


# Define categories (same as in preprocessing)
categories = {'markers': 0, 'pencilcrayons': 1, 'paints': 2}

# Preprocess the image
img = load_img(file_path, target_size=(128, 128))
# Convert the image to a numpy array
img_array = img_to_array(img)
# Normalize pixel values to [0, 1]
img_array = img_array / 255.0
# Add a batch dimension (1, height, width, channels)
img_array = np.expand_dims(img_array, axis=0)

print(len(img_array))

# # Make a prediction
# predictions = model.predict(input_image)

# # Get the predicted class index and confidence
# predicted_class = np.argmax(predictions[0])  # Index of the highest probability
# confidence = predictions[0][predicted_class]  # Probability of the prediction

# # Map the predicted class index to the class name
# predicted_label = list(categories.keys())[list(categories.values()).index(predicted_class)]

# # Output the prediction
# print(f"Predicted Label: {predicted_label}")
# print(f"Confidence: {confidence:.2f}")
