import re

def validate_credit_card(card_number):
    # 1. Structure Check: Starts with 4, 5, or 6 and is either 16 digits or 4 groups of 4 separated by '-'
    structure_pattern = r'^[456](\d{15}|\d{3}(-\d{4}){3})$'
    
    if not re.match(structure_pattern, card_number):
        return "Invalid"
    raw_digits = card_number.replace('-', '')
    if re.search(r'(\d)\1{3,}', raw_digits):
        return "Invalid"
        
    return "Valid"

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        card = input().strip()
        print(validate_credit_card(card))
