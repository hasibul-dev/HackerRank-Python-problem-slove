import sys
from html.parser import HTMLParser

class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

if __name__ == "__main__":
    # Read all input from standard input
    input_data = sys.stdin.read().splitlines()
    
    if input_data:
        n = int(input_data[0])
        html_content = "\n".join(input_data[1:n+1])
        
        parser = CustomHTMLParser()
        parser.feed(html_content)
