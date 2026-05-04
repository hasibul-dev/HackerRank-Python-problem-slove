from itertools import combinations

# Read input and split into string S and integer k
s_input, k = input().split()
k = int(k)

# Sort the string lexicographically first
# This ensures combinations are generated in sorted order
s_sorted = sorted(s_input)

# Loop through each size i from 1 up to k
for i in range(1, k + 1):
    # Generate combinations of size i
    for combo in combinations(s_sorted, i):
        # Join the tuple into a string and print
        print("".join(combo))
