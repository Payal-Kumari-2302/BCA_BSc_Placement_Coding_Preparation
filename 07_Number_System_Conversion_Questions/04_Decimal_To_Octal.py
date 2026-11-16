# Q4 - Decimal to Octal

# Problem:
# Convert a Decimal number into Octal.

# Solution:

num = int(input("Enter a Decimal number: "))

octal = ""

if num == 0:
    octal = "0"

while num > 0:

    remainder = num % 8

    octal = str(remainder) + octal

    num = num // 8

print("Octal Number:", octal)


# Output:
# Enter a Decimal number: 25
# Octal Number: 31
