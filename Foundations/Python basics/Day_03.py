# Arithmetic Operators

''' Arithmetic operators are used with numeric values to perform common mathematical operations: '''

x = 15
y = 4


print(x + y) # Addition: Adds two values
print(x - y) # Subtraction: Subtracts one value from another
print(x * y) # Multiplication: Multiplies two values
print(x / y) # Division: Divides one value by another (result is a float)
print(x % y) # Modulus: Returns the remainder of division
print(x ** y) # Exponentiation: Raises one value to the power of another
print(x // y) # Floor Division: Divides and returns the largest integer less than or equal to the result


# The Walrus Operator

'''Python 3.8 introduced the := operator, known as the "walrus operator". 
  It assigns values to variables as part of a larger expression'''

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Comparison Operators
''' Comparison operators are used to compare two values
    Comparison operators return True or False based on the comparison'''

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Chaining Comparison Operators
''' You can chain comparison operators to check multiple conditions simultaneously '''

x = 5

print(1 < x < 10)
print(1 < x and x < 10)


# Python Identity Operators
''' Identity operators are used to compare the memory locations of two objects '''

# is operator - The is operator returns True if both variables point to the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#  The is not operator returns True if both variables do not point to the same object

x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

# Difference Between is and ==
''' The == operator compares the values of both the operands and checks for value equality.
    The is operator checks whether both the operands refer to the same object in memory.'''

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)



# Python Bitwise Operators
''' Bitwise operators are used to compare (binary) numbers'''
''' The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0 '''
print(6 & 3)
''' The | operator compares each bit and set it to 1 if one of them is 1, otherwise it is set to 0 '''
print(6 | 3)
''' The ^ operator compares each bit and set it to 1 if one of them is 1 and the other is 0, otherwise it is set to 0 '''
print(6 ^ 3)
''' The ~ operator is unary and inverts all the bits '''
print(~6)
''' The << operator shifts the bits of the first operand to the left by the number of positions specified by the second operand '''
print(6 << 1)
''' The >> operator shifts the bits of the first operand to the right by the number of positions specified by the second operand '''
print(6 >> 1)
