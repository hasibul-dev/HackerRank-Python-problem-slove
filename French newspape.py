
n = int(input())
english_subs = set(map(int, input().split()))

# Read input for French newspaper subscribers
m = int(input())
french_subs = set(map(int, input().split()))

# Find the intersection of both sets
both_subs = english_subs.intersection(french_subs)

# Output the total number of students (the size of the intersection set)
print(len(both_subs))
