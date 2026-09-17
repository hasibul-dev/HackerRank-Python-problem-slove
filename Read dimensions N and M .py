import numpy as np


n, m = map(int, input().split())


my_array = np.array([list(map(int, input().split())) for _ in range(n)])

# Compute the minimum along axis 1, then find the maximum of that result
result = np.max(np.min(my_array, axis=1))

print(result)
