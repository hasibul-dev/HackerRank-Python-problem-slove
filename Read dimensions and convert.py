import numpy as np

# Read dimensions and convert them into a tuple of integers
shape = tuple(map(int, input().split()))

# Print array of zeros followed by array of ones
print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))
