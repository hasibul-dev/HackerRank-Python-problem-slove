def is_strict_superset():
    # Read the main set A
    set_a = set(map(int, input().split()))
    
    # Read the number of other sets
    n = int(input())
    
    # Check each of the N sets
    for _ in range(n):
        other_set = set(map(int, input().split()))
        
        # If set_a is not a strict superset of other_set, print False and exit
        if not (set_a > other_set):
            print("False")
            return
            
    # If it passes the check for all sets, print True
    print("True")

if __name__ == "__main__":
    is_strict_superset()
