from itertools import permutations

def print_permutations():
  
    input_data = input().split()
    S = input_data[0]
    k = int(input_data[1])

   
    S = sorted(S)

  
    perms = permutations(S, k)


    for p in perms:
        print("".join(p))

if __name__ == '__main__':
    print_permutations()
