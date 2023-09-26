''' After we create a python file then import from it then we run the program.
Then we can see a new cache file called __pycache__ is added automatically. 
This file is the compilted python file. 

The __pycache__ directory is a directory automatically created by Python to store compiled bytecode files (.pyc) 
when a Python module is imported. These compiled bytecode files are used to speed up the loading of modules and 
improve performance.

Here's how it works:
Module Compilation: When a Python module is imported for the first time, Python checks if a corresponding 
.pyc file exists in the __pycache__ directory with the same name as the module. If it doesn't find the 
.pyc file or if the source code of the module has been modified since the last compilation, Python compiles 
the module's source code into bytecode.

Bytecode Storage: The compiled bytecode is then stored in a .pyc file inside the __pycache__ directory. 
The .pyc file contains a serialized version of the bytecode that the Python interpreter can quickly load and execute.

Subsequent Imports: When the same module is imported again in the future, Python checks the __pycache__ directory 
for a corresponding .pyc file. If it finds one and the source code hasn't changed, Python loads the bytecode from 
the .pyc file instead of recompiling the source code. This results in faster module loading times.

The __pycache__ directory is typically located in the same directory as the Python script or module that is being 
executed. Its name is always __pycache__, and it contains .pyc files for each module that has been compiled. 
The naming convention for these .pyc files is as follows: 

module_name.version.pyc

module_name is the name of the Python module.
version indicates the Python version for which the bytecode was compiled.
For example, if you have a module named example.py and you are using Python 3.8, the corresponding bytecode 
file in the __pycache__ directory would be named example.cpython-38.pyc.

The use of the __pycache__ directory helps Python programs start faster since they can skip the compilation 
step for modules that haven't changed since the last run. It's also a way to separate compiled bytecode from 
the original source code, making it easier to distribute Python code without sharing the source. '''
