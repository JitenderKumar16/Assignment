# Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder

def divide(dividend, divisor):
    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1
    return quotient

a = int(input("Enter the value of Dividend: "))
b = int(input("Enter the value of Divisor: "))

print("Result:", divide(a,b))

d
