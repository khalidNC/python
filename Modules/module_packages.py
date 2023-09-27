import module_sub_directory.module_sales

from module_sub_directory.module_sales import price

from module_sub_directory import module_sales

# Accessing the fuction from module_sales module
module_sub_directory.module_sales.product_name("Bread")        # Output: Product name is Bread

# Accessing the price variable from module_sales module
print(price)                                                   # Output: 3 USD

# Accessing the function and variable on the module
module_sales.product_name("Fish")                                        # Output: Product name is Fish

# Accessing the price variable from module_sales module
print(module_sales.price)                                                # Output: 3 USD




''' Package Structure: Python supports package structures, which are directories containing a special file 
named __init__.py. These package directories can contain sub-packages and modules. When you import a module 
from a package, Python searches within the package's directory and its sub-packages for the specified module. 

Let's create a sub-directory(module_sub_directory) in Modules directory. And then create a python file
module_sales.py 

Now if we import module_sales we see problems(Alert "import module_sales") here because python does not find the module. 

To fix this issue we need to go back to the sub-directory and add a python file __init__.py 
when you add the __init__.py file python will treat the sub-directory as a package. A package is a container
of one or more modules. 

So we can say a package is a dictory and module is a file. Now we go back to the current page and prefix 
the module_name with the name of it's package(sub-directory) and .dot then the problem-alert is solved. 
e.g import module_sub_directory.module_sales

Now to use any object of the module_sales module we need to prefix the package and the module_name with .dot

In another way we can import. Using from the syntax is, from package_name.module_name import specific_object
and then you just call the object without writing the package_name.module_name everytime in your code.

we can also have a different approach. We can import the whole module from the package. Syntax,
from package_name import module_name
then call any object on module with .dot '''
