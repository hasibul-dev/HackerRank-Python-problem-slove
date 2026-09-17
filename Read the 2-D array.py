import numpy

# Read dimensions N and M
n, m = map(int, input().split())

# Read the 2-D array
my_array = numpy.array([input().split() for _ in range(n)], int)

# Compute the sum along axis 0, then find the product of that result
result = numpy.prod(numpy.sum(my_array, axis=0), axis=0)

print(result)
