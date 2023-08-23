''' There are situations where you may need to raise exceptions in your own code. 
In Python, you can raise exceptions explicitly using the raise statement. This allows 
you to signal that an error or exceptional situation has occurred in your code. 
You can either raise built-in exceptions or create your own custom exceptions. '''

''' Raising Built-in Exceptions:
To raise a built-in exception, you can use the raise statement followed by the exception 
class and an optional error message. Here's the general syntax: 
  
raise ExceptionType("Error message") '''

# Here are a couple of examples:
# Raising a ValueError
x = -5
try:
    if x < 0:
        raise ValueError("Negative numbers are not allowed")
except ValueError as error:
    print(error)
else:
    print("No exception was raised.")
    

# # Raising an IndexError
my_list = [1, 2, 3]
index = 8
try:
    if index >= len(my_list):
        raise IndexError("Index out of range")
    
except IndexError as r:
    print('Cought:', r)

else:
    print("No exception was thrown")
