import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# Create a copy and update index 2
arr_copy = arr.copy()
arr_copy[2] = 99
print("Original array after copy update:", arr)
print("Copied array:", arr_copy)

# Create a view and update index 2
arr_view = arr.view()
arr_view[2] = 99
print("Original array after view update:", arr)
print("View array:", arr_view)
