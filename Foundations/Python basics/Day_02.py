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

x = "Hello" # Any non-empty string → True
y = 0 # 0 → False

print(bool(x))
print(bool(y))


# Most Values are True

'''  Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.'''

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

# Some Values are False
''' In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. 
And of course the value False evaluates to False.'''

print(bool(False))
print(bool())

''' One more value, or object in this case, evaluates to False,
 and that is if you have an object that is made from a 
 class with a __len__ function that returns 0 or False: '''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can Return a Boolean
''' You can create functions that return a boolean value: '''
def myfunction():
    return True
print(myfunction())

# You can execute code based on the Boolean answer of a function:
def funtion():
    return False
if funtion():
    print(" YES ")
else :
    print(" NO")

''' Python also has many built-in functions that return a boolean value, like the isinstance() function,
 which can be used to determine if an object is of a certain data type '''
x = 200
print(isinstance(x,int))