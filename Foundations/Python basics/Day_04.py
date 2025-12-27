# Python Lists
''' Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets: '''

the_list = ['apple', 'banana', 'orange']
print(the_list)

# List Items

''' List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.'''

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

''' To determine how many items a list has, use the len() function:  '''

thislist = [" apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))

# List Items - Data Types

''' List items can be of any data type,A list can contain different data types '''

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]

# type() - lists are defined as objects with the data type 'list'
print(type(list1))

# The list() Constructor
''' It is also possible to use the list() constructor when creating a new list. '''

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Python Collections (Arrays)

''' There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered and changeable. No duplicate members. '''

# Python - Access List Items
''' List items are indexed and you can access them by referring to the index number '''

# Negative Indexing
''' Negative indexing means start from the end -1 refers to the last item, 
-2 refers to the second last item etc. '''

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes
''' You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items. '''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# ['cherry', 'orange', 'kiwi']
print(thislist[1:4])
# ['banana', 'cherry', 'orange']
''' Note: The search will start at index 2 (included) and end at index 5 (not included). '''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# ['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# ['cherry', 'orange', 'kiwi', 'melon', 'mango']

''' This example returns the items from "orange" (-4) to, but NOT including "mango" (-1)  '''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# ['orange', 'kiwi', 'melon']

# Check if Item Exists
''' To determine if a specified item is present in a list use the in keyword '''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# Yes, 'apple ' is in the fruits list

