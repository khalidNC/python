# class CommonFunction:

#   def __init__(self):
#     self.model = 2010

#   def auto_gear(self):
#     print("Auto Gear")


# class AllionFunctions(CommonFunction):

#   def projection_light(self):
#     print("Projection Light")

#   def light_adjustor(self):
#     print("Headlight Adjustor")


# allion = AllionFunctions()
# allion.auto_gear()
# print(allion.model)     # Output: 2010



# class AxioFunction(CommonFunction):

#   def hd_light(self):
#     print("Hd Light")

#   def fog_light(self):
#     print("Fog light")


# axio = AxioFunction()
# axio.auto_gear()
# print(axio.model)       #Output: 2010


''' In the above codes, we innitialize the artibute age = 1 in the base class CommonFunction. What if we initialize 
an attribute like engine = 1500 in AllionFucntion. Let's make the change and see below. 

It gives attribute error. Because the __init__ method in base class overrides the __init__ method of subclass.
This is called method override.

To fix this, we will use built in method super() in the __init__ method inside subclass, it allows to call any of the 
methods in the class. In this case we will call __init__ method of base class. Let's do it and see. '''

# class CommonFunction:

#   def __init__(self):
#     self.model = 2010

#   def auto_gear(self):
#     print("Auto Gear")


# class AllionFunctions(CommonFunction):

#   def __init__(self):
#     self.engine = 1500

#   def projection_light(self):
#     print("Projection Light")

#   def light_adjustor(self):
#     print("Headlight Adjustor")


# allion = AllionFunctions()
# allion.auto_gear()
# print(allion.model)     # Output: AttributeError: 'AllionFunctions' object has no attribute 'model'
# print(allion.engine)    # Output: AttributeError: 'AllionFunctions' object has no attribute 'model'



# class AxioFunction(CommonFunction):

#   def hd_light(self):
#     print("Hd Light")

#   def fog_light(self):
#     print("Fog light")


# axio = AxioFunction()
# axio.auto_gear()
# print(axio.model)       #Output: 2010


''' To fix this, we will use built in method super() in the __init__ method inside subclass, it allows to call any of the 
methods in the class. In this case we will call __init__ method of base class. Let's do it and see. '''

class CommonFunction:

  def __init__(self):
    self.model = 2010

  def auto_gear(self):
    print("Auto Gear")


class AllionFunctions(CommonFunction):

  def __init__(self):
    super().__init__()
    self.engine = "1500cc"

  def projection_light(self):
    print("Projection Light")

  def light_adjustor(self):
    print("Headlight Adjustor")


allion = AllionFunctions()
allion.auto_gear()
print(allion.model)     # Output: 2010
print(allion.engine)    # Output: 1500cc



class AxioFunction(CommonFunction):

  def hd_light(self):
    print("Hd Light")

  def fog_light(self):
    print("Fog light")


axio = AxioFunction()
axio.auto_gear()
print(axio.model)       #Output: 2010
