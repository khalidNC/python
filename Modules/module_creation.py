''' In Python, a module is a file that contains Python code, including functions, classes, and variables.
Modules are used to organize and reuse code, making it easier to manage and maintain large programs.
Python provides a straightforward way to create and use modules, allowing you to encapsulate code
into separate files for better organization and reusability. '''

''' Creating a module in Python is a simple process. You can create a module by following these steps:
1. Create a Python File: Begin by creating a new Python file with a .py extension. This file will become your module.

2. Define Functions, Classes, or Variables: Inside the Python file, define functions, classes, variables, or any other
   code that you want to encapsulate within the module. 
   
3. Save the File: Save the Python file with a meaningful name. In this example, we named it mymodule.py. '''


''' Importing a Module: Once you've created a module, you can use it in other Python scripts or programs
by importing it. Importing a module allows you to access its functions, classes, and variables. Here's how you 
can import a module: (i) You can import the intire module as an object or (ii) you can import specific object in
the module

(i) Import intire module as an object: 
1. Import the Module: In your Python script or program, use the import keyword followed by the name of the module 
(without the .py extension).

2. Access Module Content: After importing the module, you can access its functions, classes, and variables using
the module name followed by a dot (.) notation e.g module_name.method() module_name.variable_name etc. '''

# import mymodule

# # Accessing a function from the module
# message = mymodule.greet("Khalid")
# print(message)                          # Output: Hello, Khalid!


# # Accessing a variable from the module
# value_of_pi = mymodule.pi
# print(f"The value of the pi is {value_of_pi}")


''' Using Module Aliases: You can also use module aliases to give modules shorter or more convenient names 
when importing them. This can be helpful when working with modules with long names: '''

# import mymodule as mm # using alias


# # Accessing a function from the module
# message = mm.greet("Khalid Hussain")

# print(message)

# # Accessing variables from the module
# value_of_pi = mm.pi

# print(f"The value of the pi is {value_of_pi}")


''' (ii) Import specific object in the module:
Importing Specific Functions or Variables: If you only need specific functions or variables from a module,
you can import them individually using the from keyword: 
1. 'from' then the module name 
2. then 'import' then if you press "Control" button in your macbook keyword and hit "Space" bar you can see all 
   the classes, functions, variables inside the module.
3. Then you can select one or multiple objects separated with a comma. '''

from mymodule import greet, pi


# Accessing function from the module
message = greet("Khalid")          # So When you import specific function then no need to use modeule_name.dot(Notation)

print(message)                     # Output: Hello, Khalid!


# Accessing variable from the module
value_of_pi = pi

print(f"The value of the pi is {value_of_pi}")    # Output: The value of the pi is 3.14159265359


''' Note: there are some places where it is shown to import in shortcut way like from mymodule import * 
But this is a bad practice sicne this import all the objects in the module that may override with the same name. '''
