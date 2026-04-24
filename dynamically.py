if __name__ == '__main__':
  
    _ = int(input())
    
    A = set(map(int, input().split()))
  
    N = int(input())
    
  
    for _ in range(N):
       
        op_info = input().split()
        op_name = op_info[0]
        
    
        other_set = set(map(int, input().split()))
        
     
        getattr(A, op_name)(other_set)

    print(sum(A))
