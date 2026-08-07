import re

S = input().strip()
k = input().strip()

# Create a regex pattern with positive lookahead to catch overlapping matches
pattern = re.compile(rf'(?=({k}))')
matches = list(pattern.finditer(S))

if not matches:
    print((-1, -1))
else:
    for match in matches:
        start = match.start()
        end = start + len(k) - 1
        print((start, end))
