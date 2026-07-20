# Read x and k from the first line
x, k = map(int, input().split())

# Read the polynomial expression string
poly_str = input()

# Evaluate the expression given the value of x in memory
print(eval(poly_str) == k)
