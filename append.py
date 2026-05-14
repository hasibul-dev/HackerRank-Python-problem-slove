from collections import deque

# Initialize an empty deque
d = deque()

# Read the number of operations
n = int(input())

# Iterate through the operations
for _ in range(n):
    # Split the input line into a list
    command = input().split()
    
    # The first element is always the method name
    method_name = command[0]
    
    # If the command has a second element, it's the value to be passed
    if len(command) > 1:
        value = command[1]
        # getattr(d, method_name) gets the method from the deque object
        # (value) executes it with the provided argument
        getattr(d, method_name)(value)
    else:
        # Execute the method without any arguments (e.g., for pop or popleft)
        getattr(d, method_name)()

# Print the final deque elements separated by a space
print(*(d))
