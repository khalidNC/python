from Modules.module_sub_directory_one import module_intra_package


''' There are times when need to import form the sibling packages. To do so we created a new 
packages(module_sub_directory_one, module_sub_directory_two). Then created a py file
(module_intra_package.py, module_intra_package_reference.py)

Now we will import this module or bojects of this module on module_intra_package_reference.py file which is under 
a sibling package: module_sub_directory_two. So let's add some functions here and go back to the 
module_intra_package_reference.py file and import this module. 

Before import add __init__.py file here in the folder to make it a package. '''


def customer_info(first_name, last_name, contact_number):
  return f"Customer Name: {first_name} {last_name}\nMobile Phone: {contact_number}"

company_name = "ABC Corp"

print(module_intra_package.product_sku(23456))
