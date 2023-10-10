# ''' Python provides a rich set of libraries and modules for working with files.
# These libraries enable you to perform various operations on files, such as reading, 
# writing, appending, and more. Here's an overview of some of the key libraries and 
# functions for working with files in Python: '''

# ''' Built-in open() Function:
# Python's built-in open() function is used to open files. It takes two arguments: 
# the file path and the mode (e.g., 'r' for reading, 'w' for writing, 'a' for appending, etc.).
# Example: '''

# with open('example.txt', 'r') as file:
#     content = file.read()


# ''' Reading Files:
# You can read the contents of a file using methods like read(), readline(), or readlines() '''

# with open('example.txt', 'r') as file:
#     content = file.read()  # Read the entire file
#     line = file.readline()  # Read one line at a time
#     lines = file.readlines()  # Read all lines into a list


# ''' Writing and Appending Files:
# To write to a file, open it in write ('w') or append ('a') mode and use write() method. '''

# with open('example.txt', 'w') as file:
#     file.write('Hello, World!')

# with open('example.txt', 'a') as file:
#     file.write('\nAppended line')


# ''' Iterating Over Lines:
# You can iterate over the lines of a file using a for loop. '''

# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line)


# ''' File Handling in a Context:
# The with statement is commonly used to ensure proper file handling. It automatically closes 
# the file when you're done.

# Working with Binary Files:
# To work with binary files, you can use modes like 'rb' (read binary) or 'wb' (write binary) 
# when opening files. '''

# with open('image.jpg', 'rb') as binary_file:
#     image_data = binary_file.read()


# ''' File Path Handling:
# The os module provides functions for working with file paths, such as os.path.join() to create 
# file paths and os.path.exists() to check if a file exists. '''

# import os

# path = os.path.join('folder', 'file.txt')
# exists = os.path.exists(path)


# ''' Exception Handling:
# When working with files, it's important to handle exceptions, such as FileNotFoundError and PermissionError, 
# to gracefully deal with file-related issues. '''

# try:
#     with open('nonexistent.txt', 'r') as file:
#         content = file.read()

# except FileNotFoundError:
#     print("File not found.")

# except PermissionError:
#     print("Permission denied.")


''' These are the fundamental tools and concepts for working with files in Python. Depending on your specific 
use case, you may also want to explore libraries like os, shutil (for file operations), and libraries for 
working with different file formats (e.g., csv, json, pickle, sqlite3, etc.). '''


''' Few other examples: Let's say we have a file on this path modules/__init__.py 
then we can use the below methods: '''

from pathlib import Path
from time import ctime

file_path = Path("modules/__init__.py")

# check the file exit in this path
print(file_path.exists())

# to rename the file
# file_path.rename("modules/init.txt")

# Delete a file
# file_path.unlink()

# Get info about the file
print(file_path.stat())

''' OutPut:
os.stat_result(st_mode=33188, st_ino=28709821, st_dev=16777220, st_nlink=1, st_uid=501, 
st_gid=20, st_size=0, st_atime=1696929588, st_mtime=1696025383, st_ctime=1696929573) 

Output we have the result object with attributes e.g st_size=0 is the sixe of the file in bite
we have also last access time(st_atime=1696929588), last modified time(st_mtime=1696025383), time 
of creation(st_ctime=1696929573) but this is not human readable. To make it human readable we need 
to import ctime from time module line:88 

from the stat() object we can pick .st_ctime wich is the creation time. And pass the path.stat().st_ctime
in to ctime() method. Then print it. '''

print(ctime(file_path.stat().st_ctime))
# OutPut: now we get the time as Tue Oct 10 15:19:33 2023


''' Also there are couple of methods to reading data from a file:
'''

# It returns content of the file as byte object that represent binary data
print(file_path.read_bytes())

# It returns content of the file as text 
print(file_path.read_text())

# Write text and byte. write_text() function care about opening and closing file
file_path.write_text()