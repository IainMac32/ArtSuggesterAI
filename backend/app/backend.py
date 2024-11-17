import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from PIL import Image
import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Load the trained model
model = load_model('models/my_model.keras')

# Define categories (same as in preprocessing)
categories = {'markers': 0, 'pencilcrayons': 1, 'paints': 2}

# Preprocess the image
def preprocess_image(image_path, target_size=(128, 128)):
    # Load the image with the target size
    img = load_img(image_path, target_size=target_size)
    # Convert the image to a numpy array
    img_array = img_to_array(img)
    # Normalize pixel values to [0, 1]
    img_array = img_array / 255.0
    # Add a batch dimension (1, height, width, channels)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Path to the test image
image_path = 'images/test_image.jpg'

# Preprocess the image
input_image = preprocess_image(image_path)

# Make a prediction
predictions = model.predict(input_image)

# Get the predicted class index and confidence
predicted_class = np.argmax(predictions[0])  # Index of the highest probability
confidence = predictions[0][predicted_class]  # Probability of the prediction

# Map the predicted class index to the class name
predicted_label = list(categories.keys())[list(categories.values()).index(predicted_class)]

# Output the prediction
print(f"Predicted Label: {predicted_label}")
print(f"Confidence: {confidence:.2f}")
