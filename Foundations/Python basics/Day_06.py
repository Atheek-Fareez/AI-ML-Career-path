# Python - Loop Lists
# You can loop through the list items by using a for loop

list = [ 'A','B','C']
for x in list:
    print( x )
'''
A
B
C
'''

# Loop Through the Index Numbers
''' You can also loop through the list items by referring to their index number.'''
# Use the range() and len() functions to create a suitable iterable.
list = [ 'A','B','C']
for i in range(len(list)):
    print( list[i])

# While Loop
list = ['A','B','C']
i = 0
while i < len(list):
     print(list[i])
     i = i + 1


# Looping Using List
''' A shorter way to loop through the list is to use a list comprehension.'''
list = ['A','B','C']
[print(x) for x in list]




