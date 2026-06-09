import sys
from itertools import combinations

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    n = int(input_data[0])
    letters = input_data[1].split()
    k = int(input_data[2])
    
    # Generate all unique index combinations of length k
    all_combinations = list(combinations(range(n), k))
    
    # Find the 0-based indices where the letter 'a' occurs
    a_indices = {i for i, letter in enumerate(letters) if letter == 'a'}
    
    # Count how many combinations contain at least one of the 'a' indices
    favorable_outcomes = 0
    for comb in all_combinations:
        # If the intersection between the combination and 'a' indices is not empty
        if any(idx in a_indices for idx in comb):
            favorable_outcomes += 1
            
    # Calculate and format the probability to 4 decimal places (as per sample output)
    probability = favorable_outcomes / len(all_combinations)
    print(f"{probability:.4f}")

if __name__ == '__main__':
    solve()
