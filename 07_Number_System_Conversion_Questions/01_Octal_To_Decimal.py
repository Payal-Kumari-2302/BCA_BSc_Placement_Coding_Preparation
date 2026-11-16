# Q1 - Octal to Decimal

# Problem:
# Convert an Octal number into Decimal.

# Solution:

octal = input("Enter an Octal number: ")

decimal = 0
power = 0

for digit in reversed(octal):

    decimal += int(digit) * (8 ** power)
    power += 1

print("Decimal Number:", decimal)


# Output:
# Enter an Octal number: 17
# Decimal Number: 15
