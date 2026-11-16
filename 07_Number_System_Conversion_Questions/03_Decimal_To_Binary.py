# Q3 - Decimal to Binary

# Problem:
# Convert a Decimal number into Binary.

# Solution:

num = int(input("Enter a Decimal number: "))

binary = ""

if num == 0:
    binary = "0"

while num > 0:

    remainder = num % 2

    binary = str(remainder) + binary

    num = num // 2

print("Binary Number:", binary)


# Output:
# Enter a Decimal number: 13
# Binary Number: 1101
