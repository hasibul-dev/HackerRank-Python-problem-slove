# Read the number of test cases
n = int(input())

for _ in range(n):
    try:
        # Read the input and split into a and b
        a, b = input().split()
        
        # Perform integer division and print the result
        print(int(a) // int(b))
        
    except ZeroDivisionError as e:
        # Handle division by zero
        print("Error Code:", e)
        
    except ValueError as e:
        # Handle invalid literal values (like '$' or '#')
        print("Error Code:", e)
