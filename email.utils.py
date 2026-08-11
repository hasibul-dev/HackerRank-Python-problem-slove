import email.utils
import re

# Read the number of input lines
n = int(input())

pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(n):
    # Parse the line into a (name, email) tuple
    parsed = email.utils.parseaddr(input())
    email_address = parsed[1]
    
    # Check if the extracted email matches our valid regex pattern
    if re.match(pattern, email_address):
        print(email.utils.formataddr(parsed))
