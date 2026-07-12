import sys

def check_subset():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # The first element is the number of test cases
    num_test_cases = int(input_data[0])
    idx = 1

    for _ in range(num_test_cases):
        # Read Set A
        num_elements_a = int(input_data[idx])
        idx += 1
        # Extract elements for A and move the pointer
        set_a = set(input_data[idx : idx + num_elements_a])
        idx += num_elements_a

        # Read Set B
        num_elements_b = int(input_data[idx])
        idx += 1
        # Extract elements for B and move the pointer
        set_b = set(input_data[idx : idx + num_elements_b])
        idx += num_elements_b

        # Check if A is a subset of B
        print(set_a.issubset(set_b))

if __name__ == "__main__":
    check_subset()
