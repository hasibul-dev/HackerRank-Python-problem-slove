from datetime import datetime

def delta_seconds():
    # Read number of test cases
    t = int(input())
    
    # Format string corresponding to: Day dd Mon yyyy hh:mm:ss +xxxx
    # %a = Abbreviated weekday, %d = Day, %b = Abbreviated month, 
    # %Y = Year, %H:%M:%S = Time, %z = Timezone offset
    time_format = "%a %d %b %Y %H:%M:%S %z"
    
    for _ in range(t):
        t1 = input()
        t2 = input()
        
        # Convert strings to datetime objects (offset-aware)
        dt1 = datetime.strptime(t1, time_format)
        dt2 = datetime.strptime(t2, time_format)
        
        # Subtracting two datetime objects returns a timedelta object
        # total_seconds() gives the difference including days converted to seconds
        diff = int(abs((dt1 - dt2).total_seconds()))
        
        print(diff)

if __name__ == '__main__':
    delta_seconds()
