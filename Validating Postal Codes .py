import re

def validate_uid(uid):
    # Rule 1: Exactly 10 alphanumeric characters
    if not re.fullmatch(r'[a-zA-Z0-9]{10}', uid):
        return "Invalid"
    
    if len(re.findall(r'[A-Z]', uid)) < 2:
        return "Invalid"
    
    if len(re.findall(r'[0-9]', uid)) < 3:
        return "Invalid"
    
    if len(set(uid)) != len(uid):
        return "Invalid"
    
    return "Valid"

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        uid = input().strip()
        print(validate_uid(uid))
