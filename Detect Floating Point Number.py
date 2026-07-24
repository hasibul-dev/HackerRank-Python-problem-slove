import re

# Read the number of test cases
t = int(input().strip())


pattern = r'^[+-]?\d*\.\d+$'

for _ in range(t):
    s = input().strip()
    # Check if string matches the format and can be cast to float
    if bool(re.match(pattern, s)):
        try:
            float(s)
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)
