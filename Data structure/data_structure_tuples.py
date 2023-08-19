''' A tuple is an ordered collection of elements, similar to a list in many programming languages. 
However, tuples have a few key differences from lists:

Immutability: Tuples are immutable, which means their elements cannot be modified, added, or removed 
after creation. Once you create a tuple, you cannot change its contents.

Syntax: Tuples are typically defined using parentheses () and separating their elements with commas. 
For example: (1, 2, 3).

Use Cases: Tuples are often used when you have a fixed set of related values that you don't intend 
to modify. They can be used to group different types of data, and because they are immutable, they 
can be used as keys in dictionaries (whereas lists cannot). 

Remember that because tuples are immutable, you cannot modify their elements, append to them, or remove 
elements from them. If you need to change the data, you would need to create a new tuple with the updated 
values. 

Here's an example of how tuples are used in Python. '''


point = (1, 2, 3) 
points = 1, 2, 3        
# Also if we remove parenthesis Python will see this as tuple.
print(type(points))     
# See the output is <class 'tuple'>


test_tuple = 1,
print(type(test_tuple))   
# See the output is <class 'tuple'> and if we remove the comma then it is 'int'

        
# Empty tuple is just the parenthesis no object is there.
empty_tuple = ()


# Concatenate tuples
concatenate_tuple = (1, 2) + (3, 4)
print(concatenate_tuple)


# Multiplication tuple with number to repeat tuple
multiplication_tuple = (2, 3, 4) * 4
print(multiplication_tuple)


# Convert a list to a tuple. We use tuple() method, this function teaks any iterable to convert tuple
list_1 = [2, 3, 5]
converted_tuple = tuple(list_1)
print(converted_tuple)


# Another example of converting string to tuple, since string is iterable
my_stirng = "Khalid Hussain"
make_tuple = tuple(my_stirng)
print(make_tuple)
# Output we get this tuple: ('K', 'h', 'a', 'l', 'i', 'd', ' ', 'H', 'u', 's', 's', 'a', 'i', 'n')


# Accessing element of a tuple with index
my_tuple = (1, 2, 3, 'a', 'b', 'c')

print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'a'


# We can get access with range/slicing as well
print(my_tuple[1:4])


# Unpacking tuple elements
first, second, *rest = my_tuple
print(first)   # Output: 1
print(second)  # Output: 2
print(rest)    # Output: [3, 'a', 'b']


# We can also find element by 'in' operator
if "a" in my_tuple:
    print("Exsits")
else:
    print("Not exists")


# Iterating through a tuple
for item in my_tuple:
    print(item)


# Length of a tuple
length = len(my_tuple)
print(length)  # Output: 6


# Tuple is not mutable, so if try to modify/replace an element of tuple we get error
my_tuple[1] = 6
# Run the code and get TypeError: 'tuple' object does not support item assignment
