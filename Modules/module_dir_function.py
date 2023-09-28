from module_sub_directory.module_sub_package import module_shopping

''' Here we will take a look at ta powerfull built-in function dir()
Here we import a module from a package and now we can access all the functions and methods of this module
with .dot oparator '''

# module_shopping.

''' In the large project there are times things do not work as ecpected then we use dir() function for 
debuging. So let's print dir of module_shopping '''

# print(dir(module_shopping))

''' OutPut: 
['__builtins__', 
'__cached__', 
'__doc__', 
'__file__', 
'__loader__', 
'__name__', 
'__package__', 
'__spec__', 
'cart_checkout', 
'payment_method', 
'shopping_cart']

We can see this module has last 3(on the above) functions and also few other methods these are 
automatically created. Let's take a look at few of these. '''

print(module_shopping.__name__)               # Output: module_sub_directory.module_sub_package.module_shopping
print(module_shopping.__file__)               # Output: /Users/user/Desktop/Python Course/Modules/module_sub_directory/module_sub_package/module_shopping.py
print(module_shopping.__package__)            # Output: module_sub_directory.module_sub_package
