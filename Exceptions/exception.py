''' In Python, an exception is an event that occurs during the execution of a program that disrupts 
the normal flow of code. Exceptions are used to handle errors, unexpected situations, and exceptional 
conditions that might arise during the execution of a program. Python provides a robust mechanism for 
handling exceptions through the use of try, except, and related statements.

Here's how exceptions work in Python:

Exception Types:
Python has a variety of built-in exception types, such as ZeroDivisionError, TypeError, ValueError, 
FileNotFoundError, and many more. Each exception type represents a specific kind of error that can occur.

Try-Except Block:
The try block contains the code where you expect an exception to occur. If an exception occurs within the 
try block, the program jumps to the corresponding except block that handles that specific type of exception.

Handling Exceptions:
In the except block, you specify the type of exception you want to catch and handle. You can also include 
additional logic to manage the exception, such as printing an error message or taking corrective action.

Exceptions are a fundamental aspect of error handling in Python and are essential for writing robust 
and reliable code. By catching and handling exceptions, you can gracefully manage errors and prevent your 
program from crashing unexpectedly.

Here's a basic example eception error: '''

# Let's say we have a list of 3 items
my_list = [1, 2, 3]

# Now by mistake I am printing 3rd index 
# print(my_list[3])
# Output: IndexError: list index out of range


# Another example: input() method

my_age = int(input("Age: "))
print(my_age)

# Now if I input a non numeric value the program crushs 
# Output: ValueError: invalid literal for int() with base 10: 'yhg'
