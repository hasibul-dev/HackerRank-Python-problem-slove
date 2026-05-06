# Read the total number of stamps
n = int(input())

# Initialize an empty set to store unique country names
countries = set()

# Iterate through the input N times
for _ in range(n):
    # Add each country to the set
    countries.add(input().strip())

# The size of the set represents the number of distinct countries
print(len(countries))
