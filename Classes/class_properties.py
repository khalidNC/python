''' There are time we need to controll over the attribute in class. For example, we are calculating 
the total price of cost of somethings and if we provide negetive price codes will works but we need 
to wrtie the codes such a way so that it rise acception if we provide negative price. In this case,
we can use property decorator. 

In the below codes if we provide negetive price still the program runs and returns negetive results.
A simple solution to this:
1. make the attribute private. __price line-22
2. define a method to get price that returns price
3. define a method to set price, that takes an argumet, value. Here we need check if the price is negetive
   then raise an acception. Otherwise value set as price.
4. Now got back to constractor, and instead of setting price directly we need to use the set_price method
   to initialize pirce. line-23 
   
Now if we try with negetive price like, -5 then it will rise acception "Price can not be negetive." So this 
could be a simple solution. But this solution is not pythonic. In python there is a better way to achive the 
same results called "property". '''


# class Price():
#   def __init__(self, price):
#     # self.__price = price
#     self.set_price(price)
  
#   def get_price(self):
#     return self.__price
  
#   def set_price(self, value):
#     if value < 0:
#       raise ValueError("Price can not be negetive.")
#     self.__price = value

#   def total_cost(self):
#     return self.__price * 10
  
# product = Price(5)
# total_cost = product.total_cost()
# print(total_cost)


''' A Property is an object that sit infornt of an attribute and allows us to get and set the avlue 
of an attribute. Let's take a look how to define a property in the price class above. Just copy the 
above codes and paste below and define property: 

1. After we define the get and set methods, we define a class attribute with the ideal name. In this
   case, we call it "price" line-71
2. And use the builtin method property(), this function takes 4 arguments;
    a. fget: to get value of an attribute
    b. fset: to set value of an attribute
    c. fdel: to delete value of an attribute
    d. doc: for documentation
   In this case, we need supply 2 arguments get_price and set_price.
   Note: we are not calling the methods we are just referrencing to them. Line-71 
3. After defining the property we use the product.(the dot oparator, line-78) and see see the 'price' property.
4. Now we can use it like a reguler field. like print, set value(line-77). 
So property looks like a reguler attribute but internaly it has 2 methods getter and setter. '''

# class Price():
#   def __init__(self, price):
#     # self.__price = price
#     self.set_price(price)
  
#   def get_price(self):
#     return self.__price
  
#   def set_price(self, value):
#     if value < 0:
#       raise ValueError("Price can not be negetive.")
#     self.__price = value

#   price = property(get_price, set_price)

#   def total_cost(self):
#     return self.__price * 10
  
# product = Price(5)
# product.price = -6
# print(product.price)
# total_cost = product.total_cost()
# print(total_cost)


''' Note: make it more pythonic by using decorator to achive same results. Again copping the above codes and 
modifing at below: 

1. Using @property decorator for get_price method in line-99 to create property instead to explicitly 
   creating propery(price = property(get_price, set_price) delete this line of code)
2. then rename the method's name to ideal name, in this case instead get_price it should be price. 
3. Then another decorator for set price: the name of the decorator would be the name of the property(in this 
case it is 'price') then .setter so the syntax is; @<name_of_property.setter> see line-103
4. Then the method name change to the ideal name. in this case, 'price' is the name.
5. Lastly we need another modification in constractor. we have no more set_price. so we will go back to self.price
   and initialize like a regular attribute(line-97). '''

class Price():
  def __init__(self, price):
    self.price = price
  
  @property
  def price(self):
    return self.__price
  
  @price.setter
  def price(self, value):
    if value < 0:
      raise ValueError("Price can not be negetive.")
    self.__price = value

  def total_cost(self):
    return self.__price * 10
  
product = Price(5)                  # Set object for the class and supply parameter
print(product.price)                # Access computed property
product.price = 10                 # Set the computed property
total_cost = product.total_cost()   # call the function total_cost() then print to total cost
print(total_cost)


''' Let's have another example: let's say
1. we need to measure a area of a circle,
2. the radius of the circle is 4cm. 
3. if we provide negetive value for the radius still the program runs, 
4. so we need to get and set property attribute and raise acception if it is provided negative value. '''


class Circle:
  def __init__(self, radius):
    self.radius = radius

  @property
  def radius(self):
    return self.__radius
  
  @radius.setter
  def radius(self, value):
    if value < 0:
      raise ValueError("Radius can not be negative.")
    self.__radius = value

  def area(self):
    return 3.14 * self.__radius ** 2
  
c_area = Circle(4)
total_area = c_area.area()
print(total_area)
