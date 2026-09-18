import numpy as np

# Set print options for compatibility with older numpy versions on HackerRank
np.set_printoptions(legacy='1.13')

# Read dimensions
n, m = map(int, input().split())

# Read the 2-D array
my_array = np.array([input().split() for _ in range(n)], dtype=int)

# Print mean along axis 1
print(np.mean(my_array, axis=1))

# Print variance along axis 0
print(np.var(my_array, axis=0))

# Print standard deviation along axis None (flattened array)
print(np.std(my_array))
