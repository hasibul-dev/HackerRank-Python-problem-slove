import sys

def find_captain_room():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # K is the first element
    K = int(input_data[0])
    
    # The rest of the elements are the room numbers
    room_list = [int(x) for x in input_data[1:]]
    
    # Get unique room numbers
    unique_rooms = set(room_list)
    
    # Apply the mathematical formula
    captain_room = (sum(unique_rooms) * K - sum(room_list)) // (K - 1)
    
    print(captain_room)

if __name__ == '__main__':
    find_captain_room()
