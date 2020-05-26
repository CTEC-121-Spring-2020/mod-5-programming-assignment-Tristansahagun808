# Module 4
#   Programming Assignment 5
#       Prob-1.py

# <Tristan Sahagun>

# IPO
'''Input(s): whole number between 1 and 10
Process: converts integer to its roman numeral counterpart
Output: prints to terminal'''

# convert number to roman numeral
def roman(Number):
    if Number == 1:
        return 'I'
    elif Number == 2:
        return 'II'
    elif Number == 3:
        return 'III'
    elif Number == 4:
        return 'IV'
    elif Number == 5:
        return 'V'
    elif Number == 6:
        return 'VI'
    elif Number == 7:
        return 'VII'
    elif Number == 8:
        return 'VIII'
    elif Number == 9:
        return 'IX'
    elif Number == 10:
        return 'X'
    else:
        return 'N/A'

# take an input then print roman numeral
def main():
    Number = int(input("Please enter a value between 1 - 10: "))
    print(roman(Number))

# unit test function
def unitTest():
    print("Number: 1\tRoman numeral:", roman(1))
    print("Number: 2\tRoman numeral:", roman(2))
    print("Number: 3\tRoman numeral:", roman(3))
    print("Number: 4\tRoman numeral:", roman(4))
    print("Number: 5\tRoman numeral:", roman(5))
    print("Number: 6\tRoman numeral:", roman(6))
    print("Number: 7\tRoman numeral:", roman(7))
    print("Number: 8\tRoman numeral:", roman(8))
    print("Number: 9\tRoman numeral:", roman(9))
    print("Number: 10\tRoman numeral:", roman(10))
   
unitTest()
main()