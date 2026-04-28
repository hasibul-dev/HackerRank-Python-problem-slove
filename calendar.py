import calendar

# Read the input month, day, and year
# Map them to integers for the calendar functions
month, day, year = map(int, input().split())

# calendar.weekday(year, month, day) returns an integer:
# 0: Monday, 1: Tuesday, ..., 6: Sunday
day_index = calendar.weekday(year, month, day)

# calendar.day_name is an array containing day names in lowercase
# We access the day by index and convert it to uppercase as requested
print(calendar.day_name[day_index].upper())
