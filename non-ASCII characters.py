import re

def replace_symbol(match):
    symbol = match.group(0)
    if symbol == '&&':
        return 'and'
    return 'or'

n = int(input())

for _ in range(n):
    line = input()
    # Match && or || preceded and followed by a space
    result = re.sub(r'(?<= )(&&|\|\|)(?= )', replace_symbol, line)
    print(result)
