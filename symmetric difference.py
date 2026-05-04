# Read input for the first set
m = int(input())
set_a = set(map(int, input().split()))

# Read input for the second set
n = int(input())
set_b = set(map(int, input().split()))

# Calculate symmetric difference
# We can use the ^ operator or the symmetric_difference() method
sym_diff = set_a.symmetric_difference(set_b)

# Sort the resulting set and print each element on a new line
for item in sorted(sym_diff):
    print(item)
