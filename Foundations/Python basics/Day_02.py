# Python Booleans

# Python has a built-in data type called boolean, which can have one of two values: True or False.
# Boolean values are often used in conditional statements to control the flow of a program.

print(10>8)
print(10 == 9)


a = 200
b = 33

if b > a :
    print(" b is greater than a  ")
else:
    print(" b is not greater then a  ")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return,

''' Step 1: bool("Hello")

"Hello" is a string.
Python checks if the string is empty or not:
Empty string "" → False
Any non-empty string → True
"Hello" is non-empty, so: True will be output'''

print(bool("Hello"))


''' Step 2: bool(15) 

15 is an integer.
Python checks if the number is zero or not:
0 → False
Any non-zero number → True
15 is non-zero, so: True will be output '''

print(bool(15))

