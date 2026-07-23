import numpy as np

n, m = map(int, input().split())
matrix = np.array([input().split() for _ in range(n)], int)

print(np.transpose(matrix))
print(matrix.flatten())
