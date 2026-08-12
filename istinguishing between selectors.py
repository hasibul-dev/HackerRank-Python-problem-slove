import re

n = int(input())
inside_block = False

# Regex to match valid 3 or 6 digit hex codes
hex_pattern = r'#(?:[0-9a-fA-F]{3}){1,2}\b'

for _ in range(n):
    line = input()

    if '{' in line:
        inside_block = True
        continue
    elif '}' in line:
        inside_block = False
        continue
        
    # Only search for color codes inside CSS property blocks
    if inside_block:
        matches = re.findall(hex_pattern, line)
        for match in matches:
            print(match)
