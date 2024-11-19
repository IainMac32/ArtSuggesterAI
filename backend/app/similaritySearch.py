#Iain and Ryan 

import numpy as np
from scipy.spatial.distance import cdist

array_of_arrays = np.array([
    [1, 2, 3],
    [4, 5, 3],
    [7, 8, 9],
    [1, 3, 3]
])  # Put real array here

input_array = np.array([2, 3, 3]) #from angela and harrison code

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
    most_similar_index = np.argmin(distances)
    most_similar_array = filtered_arrays[most_similar_index]

    print(f"Filtered Arrays: \n{filtered_arrays}")
    print(f"Distances: {distances.ravel()}")
    print(f"Most Similar Array!: {most_similar_array}")
