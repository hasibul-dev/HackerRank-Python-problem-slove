def total_unique_subscriptions():
    # Read English newspaper subscribers
    _ = input()  # Number of English subscribers (unused)
    english_subs = set(map(int, input().split()))
    
    # Read French newspaper subscribers
    _ = input()  # Number of French subscribers (unused)
    french_subs = set(map(int, input().split()))
    
    # Find the symmetric difference between both sets
    unique_subs = english_subs.symmetric_difference(french_subs)
    
    # Output the total count of students
    print(len(unique_subs))

if __name__ == "__main__":
    total_unique_subscriptions()
