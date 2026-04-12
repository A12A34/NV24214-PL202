import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print("Reshaped to 4x3:")
print(newarr)

flat = newarr.reshape(-1)
print("Reshaped back to 1D:")
print(flat)
