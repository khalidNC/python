from pathlib import Path


# Here is the path object represents the Modules directory
path = Path("Modules")

# Few methods we can use to extract Path object value
# print(path.is_dir())              # To check is this directory returns boolean
# print(path.exists())              # To check it exist or not returns boolean
# print(path.mkdir())               # Create directory
# print(path.rmdir())               # Remove directory
# print(path.rename("module2"))     # Rename to new name


''' Method iterdir() to iterate over the directory items. With this method we can get the 
files and directories in this Path.'''

path.iterdir()

# Let's print the result and see what we get
print(path.iterdir())
# OutPut: <generator object Path.iterdir at 0x10d19dc40>

''' We get get a generator object. Generator object retruns a new value every time we iterate.
So when we working with a large list of items, instead storing this to a memory store these
in a generator object. That's the reason it returns a generator object. Since here we are working with
directory so there is posibility of having huge number of files in it. 

So we need to iterate it like, for files in path; '''


for item in path.iterdir():
  print(item)

''' OutPut:
Modules/module_sub_directory
Modules/module_compiled_python_file.py
Modules/.DS_Store
Modules/module_search_path.py
Modules/module_dir_function.py
Modules/__init__.py
Modules/module_sub_directory_one
Modules/__pycache__
Modules/module_packages.py
Modules/module_sub_packages.py
Modules/mymodule.py
Modules/module_executing_module_as_script.py
Modules/module_creation.py '''

''' Now we can convert this generator to a list. Using a list comprehension expression:
like instead iterate using square bracket[item for item in path] '''

list_of_item = [item for item in path.iterdir()]
print(list_of_item)

''' OutPut: 
[PosixPath('Modules/module_sub_directory'), PosixPath('Modules/module_compiled_python_file.py'), 
PosixPath('Modules/.DS_Store'), PosixPath('Modules/module_search_path.py'), 
PosixPath('Modules/module_dir_function.py'), PosixPath('Modules/__init__.py'), 
PosixPath('Modules/module_sub_directory_one'), PosixPath('Modules/__pycache__'), 
PosixPath('Modules/module_packages.py'), PosixPath('Modules/module_sub_packages.py'), 
PosixPath('Modules/mymodule.py'), PosixPath('Modules/module_executing_module_as_script.py'), 
PosixPath('Modules/module_creation.py')] 

We get a array of PosixPath objects. What is this? 
At the top we import Path class which is the base class of 2 classes
    1. PosixPath - for Mac
    2. WindowsPath - for window '''

''' Now we can make the list comprehension expression more useable by fileting. 
Like you only want get the directories then can use .is_dir() method in the list expression. '''


list_of_item = [item for item in path.iterdir() if item.is_dir()]
print(list_of_item)

''' OutPut: 
[PosixPath('Modules/module_sub_directory'), PosixPath('Modules/module_sub_directory_one'), 
PosixPath('Modules/__pycache__')] 

Got only the directories. '''

''' 
Use of .glob() method:
There are 2 limitations of .iterdir() methods
    1. It does not allow to search by pattern 
    2. It does not search recursively 
    
For search by pattern we need to use .glob() method. This method takes 
pattarn("*.*" or "*.py") [*.* means all files, *.py python files only] and it returns generator so
we need to use list expression e.g [item for item in path.glob("*.*")] '''

list_of_items = [p for p in path.glob("*.*")]
print(list_of_items)

''' OutPut: 
PosixPath('Modules/module_compiled_python_file.py'), 
PosixPath('Modules/.DS_Store'), 
PosixPath('Modules/module_search_path.py'), 
PosixPath('Modules/module_dir_function.py'), 
PosixPath('Modules/__init__.py'), 
PosixPath('Modules/module_packages.py'), 
PosixPath('Modules/module_sub_packages.py'), 
PosixPath('Modules/mymodule.py'), 
PosixPath('Modules/module_executing_module_as_script.py'), 
PosixPath('Modules/module_creation.py')] '''

''' For search recursively we need to change something like this;
list_of_items = [p for p in path.glob("**/*.*")] or to use rglob() short form of recursive glob
list_of_items = [p for p in path.rglob("*.*")] '''

recursive_py_files = [p for p in path.rglob("*.py")]
print(recursive_py_files)

''' OutPut: now we can see all childs files
[PosixPath('Modules/module_compiled_python_file.py'), 
PosixPath('Modules/module_search_path.py'), 
PosixPath('Modules/module_dir_function.py'), 
PosixPath('Modules/__init__.py'), 
PosixPath('Modules/module_packages.py'), 
PosixPath('Modules/module_sub_packages.py'), 
PosixPath('Modules/mymodule.py'), 
PosixPath('Modules/module_executing_module_as_script.py'), 
PosixPath('Modules/module_creation.py'), 
PosixPath('Modules/module_sub_directory/module_sales.py'), 
PosixPath('Modules/module_sub_directory/__init__.py'), 
PosixPath('Modules/module_sub_directory/module_sub_package/__init__.py'), 
PosixPath('Modules/module_sub_directory/module_sub_package/module_shopping.py'), 
PosixPath('Modules/module_sub_directory/module_intra_package_reference/__init__.py'), 
PosixPath('Modules/module_sub_directory/module_intra_package_reference/customer.py'), 
PosixPath('Modules/module_sub_directory_one/module_supplier.py'), 
PosixPath('Modules/module_sub_directory_one/__init__.py')] '''
