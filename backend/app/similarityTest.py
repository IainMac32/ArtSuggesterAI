import numpy as np

import os
print(os.listdir())  # List files in the current directory

loaded = np.load('data_np.npz')
data_np = loaded['arr_0']  # Access the array

print(len(data_np))
print(len(data_np[0]))
print(data_np[0])

print(data_np[0][49152:])
