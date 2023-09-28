# Absolute import
from module_sub_directory.module_intra_package_reference import customer

# Relative import
# from ..module_intra_package_reference import customer


def shopping_cart(int):
  if int > 0:
    return f"Product {int} is added to cart successfully"
  
def cart_checkout(payment):
  return f"Add payment method {payment}"

payment_method = "VISA"

customer_name = customer.customer_info("k", "h", 3456)
print(customer_name)
