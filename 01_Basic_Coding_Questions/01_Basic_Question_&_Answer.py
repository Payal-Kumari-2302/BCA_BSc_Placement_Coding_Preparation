# Q1 - Print Hello World
```python
print("Hello World")
```
**Output:**
```text
Hello World
```

# Q2 - Take Input and Print
```python
name = input("Enter your name: ")
print("Hello", name)
```
**Output:**
```text
Enter your name: Payal
Hello Payal
```

# Q3 - Add Two Numbers
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
```
**Output:**
```text
Enter first number: 10
Enter second number: 20
Sum: 30
```

# Q4 - Subtract Two Numbers
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Subtraction:", a - b)
```
**Output:**
```text
Enter first number: 20
Enter second number: 10
Subtraction: 10
```

# Q5 - Multiply Two Numbers
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Multiplication:", a * b)
```
**Output:**
```text
Enter first number: 10
Enter second number: 5
Multiplication: 50
```

# Q6 - Divide Two Numbers
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Division:", a / b)
```
**Output:**
```text
Enter first number: 20
Enter second number: 4
Division: 5.0
```

# Q7 - Find Remainder
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Remainder:", a % b)
```
**Output:**
```text
Enter first number: 17
Enter second number: 5
Remainder: 2
```

# Q8 - Average of Three Numbers
```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("Average:", (a + b + c) / 3)
```
**Output:**
```text
Enter first number: 10
Enter second number: 20
Enter third number: 30
Average: 20.0
```

# Q9 - Swap Using Third Variable
```python
a = 10
b = 20

temp = a
a = b
b = temp

print("a =", a)
print("b =", b)
```
**Output:**
```text
a = 20
b = 10
```

# Q10 - Swap Without Third Variable
```python
a = 10
b = 20

a, b = b, a

print("a =", a)
print("b =", b)
```
**Output:**
```text
a = 20
b = 10
```

# Q11 - Square of a Number
```python
num = int(input("Enter number: "))
print("Square:", num * num)
```
**Output:**
```text
Enter number: 5
Square: 25
```

# Q12 - Cube of a Number
```python
num = int(input("Enter number: "))
print("Cube:", num * num * num)
```
**Output:**
```text
Enter number: 3
Cube: 27
```

# Q13 - Area of Circle
```python
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
print("Area:", area)
```
**Output:**
```text
Enter radius: 5
Area: 78.5
```

# Q14 - Area of Rectangle
```python
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
print("Area:", length * breadth)
```
**Output:**
```text
Enter length: 10
Enter breadth: 5
Area: 50.0
```

# Q15 - Area of Triangle
```python
base = float(input("Enter base: "))
height = float(input("Enter height: "))
print("Area:", 0.5 * base * height)
```
**Output:**
```text
Enter base: 10
Enter height: 5
Area: 25.0
```

# Q16 - Celsius to Fahrenheit
```python
celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)
```
**Output:**
```text
Enter Celsius: 30
Fahrenheit: 86.0
```

# Q17 - Fahrenheit to Celsius
```python
fahrenheit = float(input("Enter Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Celsius:", celsius)
```
**Output:**
```text
Enter Fahrenheit: 98.6
Celsius: 37.0
```

# Q18 - Simple Interest
```python
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

si = (p * r * t) / 100
print("Simple Interest:", si)
```
**Output:**
```text
Enter principal: 1000
Enter rate: 5
Enter time: 2
Simple Interest: 100.0
```

# Q19 - Total and Percentage of Marks
```python
m1 = float(input("Enter subject 1 marks: "))
m2 = float(input("Enter subject 2 marks: "))
m3 = float(input("Enter subject 3 marks: "))

total = m1 + m2 + m3
percentage = total / 300 * 100

print("Total:", total)
print("Percentage:", percentage)
```
**Output:**
```text
Enter subject 1 marks: 80
Enter subject 2 marks: 90
Enter subject 3 marks: 70
Total: 240.0
Percentage: 80.0
```

# Q20 - Minutes into Hours and Minutes
```python
minutes = int(input("Enter minutes: "))

hours = minutes // 60
remaining = minutes % 60

print("Hours:", hours)
print("Minutes:", remaining)
```
**Output:**
```text
Enter minutes: 150
Hours: 2
Minutes: 30
```

# Q21 - Days into Years, Weeks and Days
```python
days = int(input("Enter days: "))

years = days // 365
remaining = days % 365

weeks = remaining // 7
remaining_days = remaining % 7

print("Years:", years)
print("Weeks:", weeks)
print("Days:", remaining_days)
```
**Output:**
```text
Enter days: 400
Years: 1
Weeks: 5
Days: 0
```

# Q22 - ASCII Value of Character
```python
ch = input("Enter a character: ")
print("ASCII Value:", ord(ch))
```
**Output:**
```text
Enter a character: A
ASCII Value: 65
```

# Q23 - Uppercase or Lowercase
```python
ch = input("Enter a character: ")

if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not an alphabet")
```
**Output:**
```text
Enter a character: P
Uppercase
```

# Q24 - Quotient and Remainder
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient:", a // b)
print("Remainder:", a % b)
```
**Output:**
```text
Enter first number: 17
Enter second number: 5
Quotient: 3
Remainder: 2
```

# Q25 - Final Price After Discount
```python
price = float(input("Enter price: "))
discount = float(input("Enter discount percentage: "))

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)
```
**Output:**
```text
Enter price: 1000
Enter discount percentage: 10
Discount: 100.0
Final Price: 900.0
```

# Q26 - Salary After Bonus
```python
salary = float(input("Enter salary: "))
bonus = float(input("Enter bonus: "))

total_salary = salary + bonus
print("Total Salary:", total_salary)
```
**Output:**
```text
Enter salary: 20000
Enter bonus: 3000
Total Salary: 23000.0
```

# Q27 - Electricity Bill
```python
units = float(input("Enter electricity units: "))
rate = float(input("Enter rate per unit: "))

bill = units * rate
print("Electricity Bill:", bill)
```
**Output:**
```text
Enter electricity units: 100
Enter rate per unit: 5
Electricity Bill: 500.0
```

# Q28 - Calculate Age Using Birth Year
```python
birth_year = int(input("Enter birth year: "))
current_year = 2026

age = current_year - birth_year
print("Age:", age)
```
**Output:**
```text
Enter birth year: 2004
Age: 22
```

# Q29 - Greatest of Two Numbers
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Greatest:", a)
else:
    print("Greatest:", b)
```
**Output:**
```text
Enter first number: 50
Enter second number: 30
Greatest: 50
```

# Q30 - Smallest of Two Numbers
```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < b:
    print("Smallest:", a)
else:
    print("Smallest:", b)
```
**Output:**
```text
Enter first number: 50
Enter second number: 30
Smallest: 30
```
