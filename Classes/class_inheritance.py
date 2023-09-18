''' There are times we have same funtions that are belongs with different classes. So that creates 
duplications. We make over the situation we can write a separate class with the functions that 
belong to different classes and then inherites the class with the other classes to get the functions.
The inherited class acts as parent class. Let's see how it happens; 

In the below codes, AllionFunctions class and AxioFunction class has same function auto_gear(). 
And when we create the class object and call the function it prints "Auto Gear" for both classes. '''

class AllionFunctions:

  def auto_gear(self):
    print("Auto Gear")

  def projection_light(self):
    print("Projection Light")

  def light_adjustor(self):
    print("Headlight Adjustor")


allion = AllionFunctions()
allion.auto_gear()


class AxioFunction:

  def auto_gear(self):
    print("Auto Gear")

  def hd_light(self):
    print("Hd Light")

  def fog_light(self):
    print("Fog light")


axio = AxioFunction()
axio.auto_gear()


''' We will create a separate class for the shared function and then use as inheritance. 
It is just put the CommonFunction class inside the parenthisis of the name of other classes.
And when we call the function we get same results without the duplication. 

This is the basic of the usage of class inheritance. '''

class CommonFunction:
  def auto_gear(self):
    print("Auto Gear")



# CommonFunction is Parent, Base
# AllionFunctions is Child, Subclass
class AllionFunctions(CommonFunction):

  def projection_light(self):
    print("Projection Light")

  def light_adjustor(self):
    print("Headlight Adjustor")


allion = AllionFunctions()
allion.auto_gear()
allion.light_adjustor()


class AxioFunction(CommonFunction):

  def hd_light(self):
    print("Hd Light")

  def fog_light(self):
    print("Fog light")


axio = AxioFunction()
axio.auto_gear()


''' The inheritance is not lilited with the function of base class but also other class
can inherite the attribute of base class. Let's initialize the base class and define attribute 
as car's model year. 

Now if we call the model in Allion/Axio class we will get the attribute value 2010 as return.
See line-106'''

class CommonFunction:

  def __init__(self):
    self.model = 2010

  def auto_gear(self):
    print("Auto Gear")


class AllionFunctions(CommonFunction):

  def projection_light(self):
    print("Projection Light")

  def light_adjustor(self):
    print("Headlight Adjustor")


allion = AllionFunctions()
allion.auto_gear()
print(allion.model)     # Output: 2010



class AxioFunction(CommonFunction):

  def hd_light(self):
    print("Hd Light")

  def fog_light(self):
    print("Fog light")


axio = AxioFunction()
axio.auto_gear()
print(axio.model)       #Output: 2010
