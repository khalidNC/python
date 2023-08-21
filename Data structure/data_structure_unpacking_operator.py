''' In Python, the unpacking operator * is used in several contexts to unpack elements 
from iterables like lists, tuples, and dictionaries. It's a powerful feature that 
provides flexibility in function calls, assignments, and more. The * operator is used 
in different ways depending on the context: '''

# List: If you want to print all individual elements in the list with unpacking operator
numbers = [1, 2, 3, 4]
print(numbers)
# Output is a list [1, 2, 3, 4]

print(*numbers)
# Output is a all idividual elements in th list: 1 2 3 4


''' Unpacking operator when creating a list: Normally I create a list for example with range()
and store in a variable. 
Now with unpcaking operator we can create the list by unpacking all the items of not only the list 
but also any iterable. Syntx: variable = [*iterable, *"Str"]. 

And at the same time we can unpack stirng'''
my_list = list(range(6))
unpack_my_list = [*range(6), *"Hello"]
print(my_list)
print(unpack_my_list)
# Output: [0, 1, 2, 3, 4, 5, 'H', 'e', 'l', 'l', 'o']


''' Combine lists with unpacking operator: You can use the * operator to unpack elements of multiple 
lists and concatenate them. '''

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = [*list1, *list2]
print(combined_list)  
# Output: [1, 2, 3, 4, 5, 6]

# You can also add in middle and unpack string
combined_list2 = [*list1, "the", *list2, *"Khalid"]
print(combined_list2)

''' Unpacking in Function Calls: You can use the * operator to unpack the elements of an iterable 
(like a list or tuple) and pass them as separate arguments to a function. '''

def my_function(a, b, c):
    print(a, b, c)


my_list = [1, 2, 3]
my_function(*my_list)  # Equivalent to my_function(1, 2, 3)

# Another example:
def my_function(first_name, middle_name, last_name):
    print(first_name, middle_name, last_name)


my_list = ["Md", "Khalid", "Hussian"]
my_function(*my_list)  # Unpcak the list items and pass as arguments) and output: Md Khalid Hussian


''' Unpacking in Assignment: You can use the * operator to unpack elements from an iterable into 
separate variables during assignment. '''

my_tuple = (10, 20, 30, 40, 50)
a, b, *rest = my_tuple
print(a)     # Output: 10
print(b)     # Output: 20
print(rest)  # Output: [30, 40, 50]


''' Unpacking in Dictionary Merging: In Python 3.5 and later, the ** operator can be used to unpack 
the contents of one dictionary into another during dictionary merging. '''

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  
# Output: {'a': 1, 'b': 3, 'c': 4}

# Note: when there are mulptiple items with the same key then last value(dict2) will be used. 
