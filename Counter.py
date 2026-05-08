from collections import Counter
import sys

# Read n and the words
n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]

# Count occurrences
counts = Counter(words)

# Results
print(len(counts))
print(*counts.values())
