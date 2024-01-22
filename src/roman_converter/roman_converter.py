# roman_converter.py

NUMERAL_MAPPING = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (100, "C"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

def convert_to_roman(number):
    if number <= 0:
        return ""

    for arabic, roman in NUMERAL_MAPPING: 
        if number >= arabic: 
            return roman + convert_to_roman(number - arabic)
        
        
print(convert_to_roman(3978))