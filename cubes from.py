import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    num_test_cases = int(data[0])
    idx = 1
    
    out = []
    for _ in range(num_test_cases):
        n = int(data[idx])
        # Extract the side lengths for the current test case
        cubes = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
        left = 0
        right = n - 1
        current_top = float('inf') # The base can be any size, so start with infinity
        possible = True
        
        while left <= right:
            # Pick the larger of the two outermost cubes
            if cubes[left] >= cubes[right]:
                picked = cubes[left]
                left += 1
            else:
                picked = cubes[right]
                right -= 1
            
            # If the picked cube is larger than the current top, the stack breaks
            if picked > current_top:
                possible = False
                break
            
            current_top = picked
            
        if possible:
            out.append("Yes")
        else:
            out.append("No")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
