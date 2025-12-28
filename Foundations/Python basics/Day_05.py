#Python - Change List Items

# change item value
''' You can change the value of a specific item by referring to its index number. '''

list = [ 'apple','banana','cherry' ]
list[1] = 'orange'
print(list)
#['apple', 'orange', 'cherry']

# Change a Range of Item Values
''' To change the value of items within a specific range, define a list with the new values, 
  and refer to the range of index numbers where you want to insert the new values '''

list = ['A','B','C','D','E','F','G']
list[1:3] = ['W','X']
print(list)
#['A', 'W', 'X', 'D', 'E', 'F', 'G']

''' If you insert more items than you replace, the new items will be inserted where you specified,'''
list = ['A','B','C','D','E','F','G']
list[1:3] = ['W','X','Y','Z']
print(list)
#['A', 'W', 'X', 'Y', 'Z', 'D', 'E', 'F', 'G']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# ['apple', 'blackcurrant', 'watermelon', 'cherry']

''' If you insert less items than you replace, 
the new items will be inserted where you specified,'''

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# ['apple', 'watermelon']

# Insert Items
''' To insert a new item without replacing any of the existing values,
you can use the insert() method. '''

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# ['apple', 'banana', 'watermelon', 'cherry']

# Add List Items
# Append Items
''' To add an item to the end of the list, use the append() method. '''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# ['apple', 'banana', 'cherry', 'orange']

# Extend Lists
''' To add elements from another list to the end of the current list, 
use the extend() method. '''

list1 = ['A','B','C']
list2 = ['D','E','F']
list1.extend(list2)
print(list1)
#['A', 'B', 'C', 'D', 'E', 'F']

# Add Any Iterable
''' The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.). '''
list1 = ['A','B','C']
tuple1 = ('D','E','F')
list1.extend(tuple1)
print(list1)
#['A', 'B', 'C', 'D', 'E', 'F']

# Python - Remove List Items
# Remove Specified Item
''' The remove() method removes the specified item. '''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# ['apple', 'cherry']

''' If there are more than one item with the specified value,
 the remove() method removes the first occurrence '''

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
# ['apple', 'cherry', 'banana', 'kiwi']

# Remove Specified Index
''' The pop() method removes the specified index, 
(or the last item if index is not specified). '''
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# ['apple', 'cherry']

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# ['apple', 'banana']

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# ['banana', 'cherry']

# The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) # this will raise an error because the list no longer exists.

# Clear the List
''' The clear() method empties the list. The list still remains, but it has no content. '''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# []