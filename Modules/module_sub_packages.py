import module_sub_directory.module_sub_package.module_shopping

from module_sub_directory.module_sub_package import module_shopping

from module_sub_directory.module_sub_package.module_shopping import shopping_cart, cart_checkout, payment_method

# Accessing module 
print(module_sub_directory.module_sub_package.module_shopping.shopping_cart(5))

# Accessing module as an abject
print(module_shopping.cart_checkout("Visa Card"))
print(module_shopping.payment_method)

# Accessing specific objcect 
print(shopping_cart(7))
print(cart_checkout("Master Card"))
print(payment_method)


''' There are time thats need you to split package into sub-packages. For example we have a package 
module_sub_directory.py now we created a directory module_sub_package and added a file module_shopping.py. 

Now if we import module here, python will not find it untill we add __init__.py file to the new folder. 
When you add __init__.py this will be trated as a package. 

We can also import entire module from sub-package. 

Also we can import specific function, variable form the sub-package.
 
'''