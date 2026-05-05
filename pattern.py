import re
import sys

def check_regex():
    # Read all input lines and strip trailing newlines
    input_data = sys.stdin.read().splitlines()
    
    if not input_data:
        return

    # First line is the number of test cases
    try:
        t = int(input_data[0])
    except (ValueError, IndexError):
        return

    # Iterate through each string starting from the second line
    for i in range(1, t + 1):
        regex_string = input_data[i]
        try:
            re.compile(regex_string)
            print("True")
        except re.error:
            print("False")

if __name__ == "__main__":
    check_regex()
