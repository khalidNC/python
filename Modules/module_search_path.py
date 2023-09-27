import mymodule
import sys

print(sys.path)

''' Let's we import mymodule module. Now python will look at mymodule.py file. If it does not find the module 
then python will look around other pre-define directories that come with python installation. Let's check it out.
we have built-in module called sys let's improt it. In  tghis module there is a variable called path which returns
list of directories where Python actually looks at for the finding the module. 

Now print the path and see the resutls, 
Output: 
['/Users/user/Desktop/Python Course/Modules', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python310.zip', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages'] 

It returns the list of all directories path in string. The first element represent the current directory in my machine.
After that we have library/framework ... it differs machine to machine. Since we are using mac and the path address
looks like this. 

So when we inport mymodule python will look at all this directories to find the module. As soon as it find the module
the search stops. '''

''' Now there might be a question how would we search module from sub-directory. Let's check it out in module_packages.py
file. '''

''' In Python, the module search path, also known as the "sys.path," is a list of directories that Python uses to 
locate modules when you import them in your code. Understanding how Python searches for modules is essential when 
you want to import custom modules, third-party packages, or standard library modules. The module search path is 
determined at runtime and can be modified during the execution of your script.

Here's a detailed explanation of the module search path in Python:

1. Built-in Modules: 
Python includes a set of built-in modules that are always available without any need for additional installation. 
These modules are part of the Python standard library and cover a wide range of functionalities. Examples include os, 
sys, and math. You can import them directly in your code without specifying their location.

2. sys.path: The sys.path variable is a list of directory names where Python looks for modules to import. It includes 
the following directories:

a. The current working directory: Python first searches for modules in the directory where your script is located. 
   This allows you to import modules from the same directory as your script.

b. Directories specified in the PYTHONPATH environment variable: You can set the PYTHONPATH environment variable to 
   include additional directories where Python should look for modules. This is a way to extend the module search 
   path beyond the default locations.

c. Standard library directories: Python includes directories where standard library modules are stored. These modules 
   are available for import without specifying their location.

d. Site-packages directory: This is a directory where third-party packages installed using tools like pip are stored. 
   Python automatically searches for packages and modules in this directory when you try to import them.

3. Package Structure: Python supports package structures, which are directories containing a special file 
named __init__.py. These package directories can contain sub-packages and modules. When you import a module from 
a package, Python searches within the package's directory and its sub-packages for the specified module.

4. Relative Imports: You can perform relative imports within a package to import modules from the same package or 
its sub-packages. Relative imports use dot notation to specify the module's location relative to the current module. 

      # Example of relative import within a package
      from . import module_name

5. Modifying sys.path: While it's generally not recommended, you can modify the sys.path list in your Python script to 
add or remove directories from the module search path. This can be useful in certain situations, but it should be 
done with caution, as it can lead to unexpected behavior and compatibility issues. 

      import sys

      # Add a directory to the module search path
      sys.path.append('/path/to/custom/module/directory')

      # Now you can import modules from the added directory
      import custom_module

Understanding how the module search path works in Python allows you to import modules effectively and manage the 
organization of your code. It's important to follow best practices when structuring your code and using virtual 
environments to isolate dependencies to avoid conflicts in the module search path. '''
