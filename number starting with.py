import re

pattern = r"^[789]\d{9}$"
n = int(input().strip())

for _ in range(n):
    mobile_number = input().strip()
    if re.match(pattern, mobile_number):
        print("YES")
    else:
        print("NO")
