#Iain and Ryan 

import numpy as np
from scipy.spatial.distance import cdist
from PIL import Image
import os


array_of_arrays = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 200, 110, 120, 130, 140, 150, 200],  # test 1
    [0, 0, 0, 0, 0, 0, 0, 0, 90, 100, 110, 120, 130, 140, 150, 150],  # test 2
    [5, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 200],   # test 3
])  # Put real array here

input_array = np.array([15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 200]) #from angela and harrison code

# filter arrays where the last index matches
last_index_value = input_array[-1]
filtered_arrays = array_of_arrays[array_of_arrays[:, -1] == last_index_value]

if len(filtered_arrays) == 0:
    print("No arrays match the condition on the last index.")
else:
    # don't include last index
    input_subarray = input_array[:-1]
    filtered_subarrays = filtered_arrays[:, :-1]

    distances = cdist(filtered_subarrays, input_subarray.reshape(1, -1), metric='euclidean')

    # smallest distance
    sorted_indices = np.argsort(distances.ravel())[:5]
    top_5_arrays = filtered_arrays[sorted_indices]

    print(f"Filtered Arrays: \n{filtered_arrays}")
    print(f"Distances: {distances.ravel()}")
    print(f"Most Similar Arrays!:\n {top_5_arrays}")


    i = 1
    for PixelImage in top_5_arrays:
        # image size
        image_size = (4, 4)
        image_data = PixelImage.reshape(image_size)

        # unNormalize
        if image_data.max() > 255 or image_data.min() < 0:
            image_data = ((image_data - image_data.min()) / (image_data.max() - image_data.min()) * 255).astype(np.uint8)

        image = Image.fromarray(image_data.astype(np.uint8))

        output_folder = "returnImages"
        output_path = os.path.join(output_folder, f"image_{i}.png")
        image.save(output_path)

        print(f"Image saved to {output_path}")
        i += 1
