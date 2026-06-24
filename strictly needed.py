# Read the number of English subscribers (not strictly needed for the logic, but part of input)
_ = input()
# Read the English subscribers and convert them into a set of integers
english_subs = set(map(int, input().split()))

# Read the number of French subscribers
_ = input()
# Read the French subscribers and convert them into a set of integers
french_subs = set(map(int, input().split()))

# Find the elements present only in the English set
only_english = english_subs.difference(french_subs)

# Output the total count
print(len(only_english))
