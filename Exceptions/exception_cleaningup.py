''' In Python, the finally block is used in conjunction with the try and except blocks to define 
a set of statements that will be executed regardless of whether an exception is raised or not. 
The finally block is often used to ensure that certain cleanup or closing operations are performed, 
such as closing files or releasing resources, regardless of whether an exception occurs in the try 
block or not. The syntax for using the finally block is as follows: 

try:
    # Code that might raise an exception
except SomeException:
    # Code to handle the exception
finally:
    # Code that will always be executed, regardless of whether an exception was raised or not

Here's an example to demonstrate the use of the finally block: '''

try:
    file = open("exception_cleaningup.py")
    age = int(input("Age: "))
    xfactor = 10 / age
    # file.close()
    # So the file needs to be closed after opening it. If I close() here and if try block throws-
    # exception then the file not be able to close
    # So where should write the close() method. The solution is write in finally: block at the end

except (ValueError, ZeroDivisionError):
    print("Please enter a valid age")

else:
    print("No exception is thorwn")

finally:
    file.close()



''' Another example: here in the exmaple, We open a file form my local then read it
then print content. And write the exception and I intentionally make a mistake in try block. 
And the program thorw the execption without crushing. But we need to close the file so 
we write the close() method under finally: block. 
Note: either the program throws exception or not the finally: block is executed. '''

try:
    file = open("exception_cleaningup.py", "r")   # There are few modes to open file. "r" is read mode. 
    content = file.read()                         # Then read()
    print(conten)
    # Here, I intentionally made a mistake, 'content' spelling is wrong which is a NameError exception type
    # So wriete a except block and print some message. So my program does not break.
    # then I need to close the file since this is still open.
    # So at the end I write finally block.

except FileNotFoundError:
    print("The file was not found.")

except NameError:
    print("Correct name")
    
finally:
    if 'file' in locals():
        # Check if the file is in local then close it
        file.close()  
        # Make sure to close the file even if an exception occurs or not
