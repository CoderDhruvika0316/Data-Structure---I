roman = input("Enter the roman numeral:")

def roman_to_arabic(roman_input):
    roman_numerals = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}

    result = 0

    for num in range(0, len(roman_input) - 1):
        if roman_numerals[roman_input[num]] < roman_numerals[roman_input[num + 1]]:
            result -= roman_numerals[roman_input[num]]
        else:
            result += roman_numerals[roman_input[num]]

    return result + roman_numerals[roman_input[-1]]

print(f"The Arabic value of {roman} is : {roman_to_arabic(roman)}")