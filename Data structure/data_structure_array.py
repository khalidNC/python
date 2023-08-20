from array import array


''' The list with large sequence of number python has a more effecient tata type 
called array. The takes less memory and performs little bit faster than list. 

We need to import array form array module. 
The array syntax is, array(typecode, initializer) >= new array
the typecode will ditermine which type of data will in the array. 
If we search in google 'python array typecode' or on this 
link: https://docs.python.org/3/library/array.html we can see the typecode. '''


numbers = array("i", [1, 2, 3, 4])
print(numbers)

''' Now can modify the array as we can do with list: '''
# Append item at the last in array
numbers.append(5)
print(numbers)


# Insert item any position by index in array
numbers.insert(0, 5)
print(numbers)


# Pop item(remove from the last) from array
numbers.pop()
print(numbers)


# Pop item(by index) from array
numbers.pop(0)
print(numbers)


# Remove item(from any specific element) from array
numbers.remove(2)
print(numbers)

# Access item by index
print(numbers[0])


# Replace element with same type data by index. e.g the list is, numbers = ("i", [1, 3, 4])
numbers[1] = 2
print(numbers)    # output: array('i', [1, 2, 4])
