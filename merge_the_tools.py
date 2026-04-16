def merge_the_tools(string, k):
   
    for i in range(0, len(string), k):
   
        substring = string[i:i+k]
        
  
        unique_string = "".join(dict.fromkeys(substring))
        
        print(unique_string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
