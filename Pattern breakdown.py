import re

vowels = "aeiouAEIOU"
consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

pattern = rf"(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])"

matches = re.findall(pattern, input())

if matches:
    print("\n".join(matches))
else:
    print(-1)
