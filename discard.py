# Read the number of elements in the set
n = int(input())

# Read the initial elements and convert them into a set of integers
s = set(map(int, input().split()))

# Read the number of commands
num_commands = int(input())

# Process each command
for _ in range(num_commands):
    # Split the input into the command name and the optional value
    command = input().split()
    cmd_name = command[0]
    
    if cmd_name == 'pop':
        s.pop()
    elif cmd_name == 'remove':
        # Convert the second part of the input to an integer for the value
        s.remove(int(command[1]))
    elif cmd_name == 'discard':
        s.discard(int(command[1]))

# Output the sum of the remaining elements in the set
print(sum(s))
