from pathlib import Path


''' How to work with files and directories in python:
We will look at here on the path class because this is the foundation of working with files and
directories. 

1. So from the pathlib module we import path class
2. Then we can create path object in few different ways:
      a. We can create object with absulote path. Path object creation syntax for mac: Path("/usr/local/bin")
      b. Create path object that represents the current flder syntax: Path()
      c. Also with relative path syntax: Path("current_folder/sub_folder/__init__.py")
      d. We can also combine path object together: Path() / Path("sub_folder")
      e. Also combine path object with string: Path() / "sub_folder" / "__init__.py" 
      d. We can also get the home directory of the current user, syntax: Path.home(), it retruns home directory

Here we use Path("sub_folder/__init__.py") as example. So let's create an object path for Path class. 
There are lots of usefull members of the Path class we can vist here: https://docs.python.org/3/library/pathlib.html
to get them. '''

# Path("/usr/local/bin")
# Path()
# Path("modules/module_sub_directory/__init__.py")
# Path() / Path("module_sub_directory")
# Path() / "module_sub_directory" / "__init__.py"
# Path.home()


path = Path("modules/module_sub_directory/__init__.py")

# To check the file exist or not. Output: boolean(True/False)
print(path.exists())

# To check this path represents a file
print(path.is_file())

# To check this path represents a directory
print(path.is_dir())

# We can also extract individual component of this path, which is very useful. For example;
print(path.name)      # Output: __init__.py

# We also have stem, which retruns file name without the file extension
print(path.stem)      # Output: __init__

# If we want the extension only
print(path.suffix)    # Output: .py

# We can get the name of the parent directory
print(path.parent)    # modules/module_sub_directory

# Another useful methods with_name() and we can use the to create new path object based on the existing path
# the only change with the name and the extension of the file. Let's say if we pass "file.txt" in the method
path = path.with_name("file.txt")
print(path)           # Output: modules/module_sub_directory/file.txt

# We can also get the absulote value of the path here
print(path.absolute())    
''' Output: /Users/user/Desktop/Python Course/modules/module_sub_directory/file.txt 
this is the absulote value of the file. This file does not exist this only represent it's path. '''

# Similar to the with_name there is another method with_suffix
path = path.with_suffix(".txt")
print(path)

''' OutPut: modules/module_sub_directory/__init__.txt so we get the extension of the file with .txt
Note: we do not change the file extension this only represents the path object. '''
