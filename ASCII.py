n = int(input())
s = sorted(list(set(map(int, input().split()))))
num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    action = command[0]
    
    if action == "pop":
        if s:
            s.pop(0)
    elif action == "remove":
        val = int(command[1])
        if val in s:
            s.remove(val)
        else:
            raise KeyError(val)
    elif action == "discard":
        val = int(command[1])
        if val in s:
            s.remove(val)

print(sum(s))
