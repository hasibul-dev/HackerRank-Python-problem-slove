import re

vowels = "aeiouAEIOU"
consonants = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

# Pattern breakdown:
# (?<=[consonants]) -> Lookbehind assertion: preceded by a consonant
# ([vowels]{2,})     -> Match: 2 or more vowels
# (?=[consonants])  -> Lookahead assertion: followed by a consonant
pattern = rf"(?<=[{consonants}])([{vowels}]{{2,}})(?=[{consonants}])"

matches = re.findall(pattern, input())

if matches:
    print("\n".join(matches))
else:
    print(-1)
