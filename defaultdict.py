from collections import defaultdict

# Read n and m
n, m = map(int, input().split())

# Initialize defaultdict with a list as the default factory
d = defaultdict(list)

# Read Group A and store indices
for i in range(1, n + 1):
    word = input().strip()
    d[word].append(str(i))

# Read Group B and check against Group A
for _ in range(m):
    word_b = input().strip()
    
    if word_b in d:
        # Join the list of indices with a space
        print(" ".join(d[word_b]))
    else:
        # Word not found in Group A
        print("-1")
