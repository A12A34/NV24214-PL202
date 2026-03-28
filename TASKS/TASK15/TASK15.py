import numpy as np

# Task 15: Concatenate two 2D arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Concatenate the two 2D arrays vertically (along axis 0)
result = np.concatenate((arr1, arr2), axis=0)
print(result)

# Alternative: Use np.vstack to stack vertically
# result = np.vstack((arr1, arr2))
# print(result)

# Alternative: Use np.hstack to stack horizontally
# result = np.hstack((arr1, arr2))
# print(result)
