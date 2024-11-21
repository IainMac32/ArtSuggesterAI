#Iain and Ryan 

import numpy as np
from scipy.spatial.distance import cdist
from PIL import Image
import os


loaded = np.load('data_np.npz')
data_np = loaded['arr_0']  # Access the array

array_of_arrays = data_np

input_array = array_of_arrays[0] #from angela and harrison code


# filter arrays where the last index matches
last_index_value = input_array[49152:49155]
filtered_arrays = array_of_arrays[np.all(array_of_arrays[:, 49152:49155] == last_index_value, axis=1)]


if len(filtered_arrays) == 0:
    print("No arrays match the condition on the last index.")
else:
    # don't include last index
    input_subarray = input_array[49155:]

    filtered_subarrays = filtered_arrays[:, 49155:]

    distances = cdist(filtered_subarrays, input_subarray.reshape(1, -1), metric='euclidean')

    # smallest distance
    sorted_indices = np.argsort(distances.ravel())[:5]
    top_5_arrays = filtered_arrays[sorted_indices]

    print(f"Filtered Arrays: \n{filtered_arrays}")
    print(f"Distances: {distances.ravel()}")
    print(f"Most Similar Arrays!:\n {top_5_arrays}")


    i = 1
for PixelImage in top_5_arrays:
    # Ensure the array represents RGB data
    PixelImage = PixelImage[:49152]  # This line ensures you use the first 49152 values
    image_size = (128, 128, 3)  # Shape for an RGB image
    image_data = PixelImage.reshape(image_size)

    # unNormalize
    if image_data.max() > 255 or image_data.min() < 0:
        image_data = ((image_data - image_data.min()) / (image_data.max() - image_data.min()) * 255).astype(np.uint8)

    # Convert to image
    image = Image.fromarray(image_data, 'RGB')

    # Save the image
    output_folder = "returnImages"
    os.makedirs(output_folder, exist_ok=True)  # Ensure the output folder exists
    output_path = os.path.join(output_folder, f"image_{i}.png")
    image.save(output_path)

    print(f"Image saved to {output_path}")
    i += 1
