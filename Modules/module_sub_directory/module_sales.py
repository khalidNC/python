# print("Sales is initialized!", __name__)        
# This code will print the text in terminal when this module in imported to somewhere eles and just executed
# For example we imported this module on "module_executing_module_as_script.py" file and run python command
# the __name__ built-in magic method return the name of the moudle
# If you run this file now this will print: "Sales is initialized! __main__" instead module anme shows __main__
# Now instead of the print instruction, if we write a code block at bottom then this file can run as script and module


def product_name(self):
  print(f"Product name is {self}")

price = "3 USD"


''' This block of code run when we execute this module as script. for example 
we execute this module with python commad python modules/module_sub_directory/module_sales.py
then it executed and print this "Product name is Food_1" terminal. 

But when this module is imported to somewhere else then this block will not executed. '''

if __name__ == "__main__":
  print("Sales is Initialized!")
  product_name("Food_1")
