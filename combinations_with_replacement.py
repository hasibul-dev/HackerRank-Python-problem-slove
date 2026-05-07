from itertools import combinations_with_replacement

# Read the input and split into string S and integer k
s_input, k_input = input().split()
k = int(k_input)

# Sort the string lexicographically first
sorted_s = sorted(s_input)

# Generate combinations with replacement of length k
combinations = combinations_with_replacement(sorted_s, k)

# Print each combination joined as a string
for combo in combinations:
    print("".join(combo))
