# Read the number of elements (n)
n = int(input())

# Read the set elements and convert to integers
s = set(map(int, input().split()))

# Read the number of commands (N)
num_commands = int(input())

# Process each command
for _ in range(num_commands):
    # Split input into command and optional argument
    # e.g., "pop" -> ["pop"] or "remove 9" -> ["remove", "9"]
    choice = input().split()
    
    if choice[0] == 'pop':
        s.pop()
    elif choice[0] == 'remove':
        # Using discard here or wrapping in try/except 
        # handles the specific environment quirks of PyPy
        try:
            s.remove(int(choice[1]))
        except KeyError:
            pass
    elif choice[0] == 'discard':
        s.discard(int(choice[1]))

# Final output: sum of remaining elements
print(sum(s))
