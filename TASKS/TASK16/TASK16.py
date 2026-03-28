import numpy as np

# Task 16: Splice array into 2 dimensional arrays into 2 parts
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

# Split the array into 2 equal parts along axis 0
result = np.split(arr, 2)

print("Part 1:")
print(result[0])
print("\nPart 2:")
print(result[1])

# Alternative: Using array slicing
# part1 = arr[:3]
# part2 = arr[3:]
# print("Part 1:")
# print(part1)
# print("\nPart 2:")
# print(part2)
