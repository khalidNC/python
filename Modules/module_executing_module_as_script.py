from module_sub_directory.module_sales import product_name

''' Just after import the module_sales module and run the pythom command 
then it will print the print instruction on the moude. 
in this case the output is : Sales is initialized! 

Now we can do the same on package __init__.py file 
In this case. the package "module_sub_directory" it's __init__.py file 
I instructed print("Module Sub Directory is Initialized!") 

Then come back to this page and again execute with python command.
And the output I get: Module Sub Directory is Initialized! in terminal.

Let's take this to next level. Go back to the module_sales and use the __name__
(to get the module name) magic method in print instruction to get the name of the module
when we execute this file in the terminal. 
And the output: Sales is initialized! module_sub_directory.module_sales 

However, if we go back to the module_sales.py module and run the file it prints 
the name of the module is __main__'''

product_name("Mint")