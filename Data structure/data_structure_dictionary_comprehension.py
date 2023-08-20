''' Dictionary comprehension in Python is a concise way to create dictionaries 
by specifying the key-value pairs using a compact syntax. It's similar to list 
comprehension but is used to construct dictionaries. This feature allows you to 
create dictionaries in a more readable and efficient manner compared to traditional loops.

The general syntax for dictionary comprehension is as follows:

{key_expression: value_expression for element in iterable} '''

# Creating a dictionary using dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num ** 2 for num in numbers}

print(squared_dict)
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

''' In this example, num is the loop variable that takes on each value from the numbers list. 
The num: num ** 2 expression creates a key-value pair where the key is the number itself, and 
the value is the square of that number. '''

''' If we create the dictionary in normal way, then this will be like; '''
numbers = [1, 2, 3, 4, 5]
values = {}
for num in numbers:
    values[num] = num ** 2

print(values)

# So instead of 3 lines code we can write the comprehension in 1 line code.
