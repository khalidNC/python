''' There are times when need to import form the sibling packages. To do so we created a new 
package(module_intra_package_reference). Then created a py file(customer.py)

Now we will import this module(customer) or bojects of this module on module_shopping.py file which is under 
a sibling package: module_sub_package. So let's add some functions here and import the module on 
module_shopping. 

Before import add __init__.py file here in the folder to make it a package. '''


def customer_info(first_name, last_name, contact_number):
  return f"Customer Name: {first_name} {last_name}\nMobile Phone: {contact_number}"

company_name = "ABC Corp"
