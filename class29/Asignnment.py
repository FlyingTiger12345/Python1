def romans(num):
    symbols = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    roman = ''
    for value, symbol in symbols:
        while num >= value:
            roman += symbol
            num -= value

    return roman

# Define the input integer
number = 6777

print('Input integer number:', number)

roman_numeral = romans(number)
print(f"The Roman numeral representation of {number} is: {roman_numeral}")