import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
     
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        # Ignore empty newline data
        if data != '\n':
            print(">>> Data")
            print(data)

if __name__ == '__main__':
    # Read all lines from input
    n = int(input())
    html_code = ""
    for _ in range(n):
        html_code += input().rstrip() + '\n'
        
    parser = MyHTMLParser()
    parser.feed(html_code)
    parser.close()
