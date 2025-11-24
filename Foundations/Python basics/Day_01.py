# Merged file: Day_01.py
# This file is an automated merge of Day_01.py .. Day_06.py
# Original files were concatenated in order. Review before running —
# the merged script may require third-party packages (numpy, scipy, matplotlib)
# and may open plots or have duplicate top-level side effects.

# ----- Begin Day_01.py -----
if 5 > 2 :
 print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!")
 print("Fivehjgjgkjhjh is greater than two!")

print("Hello World!",  end = " ")
print("I will print on the same line.")

print ( "I am",35,"years old.")

x = 5
print(x)

x = str(3)
y = int(3)
z = float(3)
print(x,y,z)
print(type(x),type(y),type(z))


fruits = ("apple", "banana", "cherry")
x, z, y = fruits
print(x,y,z)

x = str(5)
y = " John"
print(x  +  y)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

print("Hello","World")

x = 'atheek'
def myfunc():
    global x
    x = 'appchi'
    print("Python is " + x)
myfunc()
print("Python is " + x)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# ----- End Day_01.py -----


# ----- Begin Day_02.py -----
"""
   ✅ 1. Text Type: str

str (string) means text — letters, words, sentences.

Example:

name = "Atheek"


Strings are always inside quotes " ".

✅ 2. Numeric Types

These are used for numbers.

a) int → whole numbers

No decimals.

age = 20

b) float → decimal numbers
height = 5.7

c) complex → numbers with a real + imaginary part

Used rarely in simple programs.

z = 3 + 4j

✅ 3. Sequence Types

These store multiple items.

a) list → changeable, ordered

You can add, remove, edit items.

fruits = ["apple", "banana", "orange"]

b) tuple → ordered, NOT changeable

Fixed data.

colors = ("red", "green", "blue")

c) range → sequence of numbers

Common in loops.

numbers = range(5)   # 0,1,2,3,4

✅ 4. Mapping Type: dict

Dictionary = key → value pairs
Like a real dictionary: word → meaning

person = {
    "name": "Atheek",
    "age": 21
}

✅ 5. Set Types

Sets = items with no duplicates and not ordered.

a) set → changeable
unique_nums = {1, 2, 3}

b) frozenset → NOT changeable
fixed_set = frozenset({1, 2, 3})

✅ 6. Boolean Type: bool

Only two values:

True
False


Used a lot in conditions:

5 > 2   # True

✅ 7. Binary Types

Used for raw data, files, images, network packets.

a) bytes

Fixed bytes:

data = b"Hello"

b) bytearray

Like bytes, but changeable.

arr = bytearray(5)

c) memoryview

For accessing parts of binary data without copying.

mv = memoryview(bytes(5))

✅ 8. None Type: NoneType

None means no value or empty value.

Example:

result = None


Used when:

A function has no return value

A variable is intentionally empty
"""
from operator import truediv

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""
# int
x = 5
print ( type(x))
# complex
x = 1j
print ( type(x))
# list
x = ["apple","banana","cherry"]
print ( type(x))
# tuple
x = ("apple","banana","cherry")
print ( type(x))
# range
x = range(6)
print(type(x))
# dict
x = { "name" : "John" , "age" : 36}
print(x)
print(type(x))
# set
x = { "apple" , "banana" , "cherry" }
print(x)
print(type(x))
# frozenset
x = frozenset({"apple" , "banana" , "cherry"})
print(x)
print(type(x))
# bool
x = True
print(x)
print(type(x))
# bytes
x = b"Hello"
print(x)
print(type(x))
# bytearray
x = bytearray(5)
print(x)
print(type(x))
x = memoryview(bytes(5))
print(x)
print(type(x))
x = None
print(x)
print(type(x))

# exercise
x = 2<5
print(x)

# type cast
#convert from int to float:
x = 2
a = float(x)
print(a)

#convert from int to complex:
c = complex(x)
print(c)
print(type(c))

import random
print(random.randrange(1,10))

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])
print(a[0])
print(a)

for x in "banana":
  print(x)

# check length
a =  "Atheek"
print(len(a))

# check string
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Day 02 part 2
# Machine learnings

import numpy

# mean
speed = [99,86,87,88,111,86,103,87,78,86]
X = numpy.mean(speed)
print(X)

speed = [86,87,88,86,87,85,86]
X = numpy.mean(speed)
print(X)


# median
speed = [99,86,87,88,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)

# mode
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)


# standard devision
speed = [86,87,88,86,87,85,86]
X = numpy.mean(speed)
print(X)
Y = numpy.std(speed)
print(Y)

speed = [32,111,138,28,59,77,97]
x = numpy.std(speed)
print(x)

# variance
speed = [32,111,138,28,59,77,97]
x = numpy.var(speed)
print(x)
# ----- End Day_02.py -----


# ----- Begin Day_03.py -----
'''
* Data Distribution
Earlier in this tutorial we have worked with very small amounts of data in our examples, just to understand the different concepts.

* In the real world, the data sets are much bigger, but it can be difficult to gather real world data, at least at an early stage of a project.

* How Can we Get Big Data Sets?
To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.

'''

# Create an array containing 250 random floats between 0 and 5:

import numpy
import matplotlib.pyplot as plt
x = numpy.random.uniform(0.0, 5.0, 250)
print(x)
plt.hist(x,5)
plt.show()

'''
Normal Data Distribution

In the previous chapter we learned how to create a completely random array, of a given size, and between two given values.
In this chapter we will learn how to create an array where the values are concentrated around a given value.
In probability theory this kind of data distribution is known as the normal data distribution, or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.
'''

x = numpy.random.normal(5.0,1.0,100000)
plt.hist(x,100)
plt.show()

'''
A scatter plot is a diagram where each value in the data set is represented by a dot.
The Matplotlib module has a method for drawing scatter plots, it needs two arrays of the same length, one for the values of the x-axis, and one for the values of the y-axis:
'''

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.show()

'''
Random Data Distributions

In Machine Learning the data sets can contain thousands-, or even millions, of values.
You might not have real world data when you are testing an algorithm, you might have to use randomly generated values.
As we have learned in the previous chapter, the NumPy module can help us with that!
Let us create two arrays that are both filled with 1000 random numbers from a normal data distribution.
The first array will have the mean set to 5.0 with a standard deviation of 1.0.
The second array will have the mean set to 10.0 with a standard deviation of 2.0:

'''

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 1000)
y = numpy.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()
# ----- End Day_03.py -----


# ----- Begin Day_04.py -----
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)

a = "Hello, World!"
print(len(a))

txt = " Atheek is a good guy "
if "Atheek"  in txt:
 print("atheek in txt")

txt = " Atheek is a good guy "
if "atheek" not  in txt:
 print("atheek not in txt")
# ----- End Day_04.py -----


# ----- Begin Day_05.py -----
# slicing string
b  = "Hello, world!"
print (b[2:5])
print(b[:5])
print(b[2:])

print(b[-5 : -2]) # negative indexing

# Python - Modify Strings

# Upper case
a = "Hello, World!"
print(a.upper())

# Lower case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = " hello, world! "
print(a.strip())

# Replace String
a = "Hello, World!"
print(a.replace("H" , "J"))

# Split String

a = "Hello World!"
print(a.split("e"))

# String Concatenation

a = "Hello"
b = "World"
c = a + " " + b
print(c)
# ----- End Day_05.py -----


# ----- Begin Day_06.py -----
# Python - Format - Strings
# String Format

# F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
# format()
print(txt.format())

age = 23
txt = f"My name is Atheek, I am {age}"
print(txt)

price = 40
txt = f"The price is {price} dollars "
print(txt)

txt = f"The price is { 45 * 2 }  dollars"
print(txt)

x = 9
print(f"The price is {x:.2f} dollars")

# Escape characters

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters used in Python:
# Single Quote
txt = ' It\'s sunny day.'
print(txt)

# \\\tBackslash
txt = "This is backslash symbol: \\"
print(txt)

# String Methods

a = " atheek "

# capitalize()
'''Look at the first character: make it uppercase.
Make all the other letters lowercase.
Return the new string.'''
print(a.capitalize())

# casefold()
'''Turn the whole string into a very aggressive lowercase form.
Make special letters (like German \u00df) become simpler forms.
Return the simplified lowercase string'''
print(a.casefold())

# center()
'''Calculate how many spaces are needed left and right to reach the total width.
Add those spaces around the text so it sits centered.
Return the padded string'''
print(a.center(10,'+'))

# count()
'''Count how many times the word "e" appears in the string.
Return the number'''
print(a.count('e'))

# endcode()
'''Turn the text into a sequence of bytes using the chosen code (utf-8 by default).
Return the bytes object (starts with b'...').
Useful to save or send text in binary form.'''
print(a.encode())

# endswith()
'''Check if the string ends with the letter "k".'''
print(a.endswith('k'))

# expandtabs()
'''Replace all tab characters with spaces, using a tab size of 2 spaces.'''
b = "H\te\tk"
print(b.expandtabs(18))

# find()
'''Find the first position occurrence of the letter "e" in the string.'''
print(a.find('e'))

# format()
'''Insert the value 10 into the placeholder {}.'''
d=80
txt = f"The price is {d} dollars"
print(txt)
txt = "The price is {} dollars"
print(txt.format(10))

# format_map()
'''Use a dictionary to insert values into the placeholders.'''
person = {'fname': 'Atheek', 'age': 23}
txt = "My name is {fname}, I am {age}"
print(txt.format_map(person))
# ----- End Day_06.py -----

