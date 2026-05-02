from collections import OrderedDict

def calculate_net_prices():
    # Initialize the ordered dictionary
    item_report = OrderedDict()
    
    try:
        # Read number of items
        n = int(input())
        
        for _ in range(n):
            # Read line and split from the right once to separate name and price
            data = input().rsplit(' ', 1)
            item_name = data[0]
            price = int(data[1])
            
            # If item exists, add to current total; otherwise, initialize it
            if item_name in item_report:
                item_report[item_name] += price
            else:
                item_report[item_name] = price
        
        # Print results in the order they were first inserted
        for item, net_price in item_report.items():
            print(f"{item} {net_price}")
            
    except EOFError:
        pass

if __name__ == "__main__":
    calculate_net_prices()
