from itertools import groupby

# Read the input string
s = input().strip()

# Group consecutive characters and format the output
output = []
for key, group in groupby(s):
    # key is the character, len(list(group)) is the number of consecutive occurrences
    count = len(list(group))
    output.append(f"({count}, {key})")

# Print the result joined by a single space
print(" ".join(output))
