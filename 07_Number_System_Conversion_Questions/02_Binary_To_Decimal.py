# Q2 - Binary to Decimal

# Problem:
# Convert a Binary number into Decimal.

# Solution:

binary = input("Enter a Binary number: ")

decimal = 0
power = 0

for digit in reversed(binary):

    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal Number:", decimal)


# Output:
# Enter a Binary number: 1011
# Decimal Number: 11
