''' The with statement in Python is used to simplify the management of resources, 
such as files or network connections, by automatically taking care of setup and 
cleanup operations. It ensures that resources are properly released when they are 
no longer needed, even in the presence of exceptions.

The syntax of the with statement is as follows: 

with context_manager as variable:
    # Code block that uses the resource 
    
Here, the context_manager is an object that supports the context management protocol, 
and the variable is where the resource is assigned. When the with block is entered, 
the resource is set up (if needed), and when the block is exited (whether normally or 
due to an exception), the resource is automatically cleaned up.

Note: if we use with statement the finally: block is no longer to use.

Here's an example using the with statement to work with files: '''

# # We have alreday a program to open, read, and finally: close file. Let's take a another look.
# try:
#     file = open("exception.py", "r") 
#     content = file.read()
#     print(content)

# except FileNotFoundError:
#     print("File was not found.")

# except NameError:
#     print("Name Correctin is Needed")

# else:
#     print("No exception was thrown")
    
# finally:
#     if 'file' in locals():
#         file.close()


''' Now use the with statement to open file. And this with statement will close the file either there
is exception thrown or not. '''

try:
    with open("exception.py", "r") as file:
      content = file.read()
      print(content)

except FileNotFoundError:
    print("File not found")

except NameError:
    print("Correct the name")

else:
    print("No exception was thrown")


''' In this example:

The open() function is used to open the file "exception.py" in read mode ("r").
The with statement is used to create a context in which the file is automatically closed 
when the block is exited. Inside the with block, the file's content is read and printed.
Once the block is exited (after the content is read or in case of an exception), 
the file is automatically closed, releasing any associated resources.

Using the with statement provides several benefits:

It ensures proper cleanup of resources, even if exceptions are raised.
It makes the code more concise and readable.
It reduces the chance of forgetting to close resources, which can lead to memory leaks or other issues.
You can use the with statement with various built-in or custom context managers, including files, 
network connections, and more. It's a recommended practice for managing resources in a clean and efficient manner. '''


''' Now here might be a question that how Python exactly works(release/close the file) under the hood? 
In the above example, look at file object the file. object, it has method started with 2underlines --class__ , 
__dict__ , __exit__ , __enter__ and many. These are define as magic methods in Python.
If the object that has __exit__ and __enter__ methods we said that context management protocol. So if an 
object support context management protocol or in other world if an object has these 2 methods then we can
use this object in with statement and Python automaticaly calls the __exit__ method and the release the
internal resources. This is how the close file works and we do not need the finally block if we use with
statement. '''

"""
try:
    with open("exception.py", "r") as file:
      content = file.read()
      print(content)
      file.__exit__       # Magic method
      file.__enter__

except FileNotFoundError:
    print("File not found")
"""

''' Now if we want to open, read, or write multiple internal resources then write open() as resource 
with comma separated. '''

"""
try:
    with open("exception.py", "r") as file, open("exception_handling.py") as terget:
      content = file.read()
      print(content)

except FileNotFoundError:
    print("File not found")
"""