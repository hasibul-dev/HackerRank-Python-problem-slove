from itertools import product

def maximize_equation():
    # Read K and M
    k, m = map(int, input().split())
    
    # Read the K lists, squaring the elements and taking modulo M immediately
    # We use a set to automatically remove duplicates, minimizing the combination pool
    lists = []
    for _ in range(k):
        row = list(map(int, input().split()))
        # row[0] is the number of elements, row[1:] are the actual elements
        squared_mods = { (x ** 2) % m for x in row[1:] }
        lists.append(squared_mods)
    
    # Generate all possible combinations of picking one element from each processed list
    max_value = 0
    for combination in product(*lists):
        # Sum the pre-computed (x^2 % m) values and take the final modulo m
        current_sum = sum(combination) % m
        if current_sum > max_value:
            max_value = current_sum
            
    print(max_value)

if __name__ == "__main__":
    maximize_equation()
