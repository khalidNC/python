''' Polymorphism is a fundamental concept in object-oriented programming that allows objects 
of different classes to be treated as objects of a common superclass. It promotes flexibility, 
code reuse, and the ability to work with different types of objects in a uniform way. In Python, 
polymorphism is achieved through method overriding and duck typing. Here's an explanation of 
polymorphism in Python: '''

# from abc import ABC, abstractmethod       # import ABC class and abstract method from abc module


# class UIControl(ABC):                 # Created a base class, and inheritated ABC class
#   @abstractmethod                     # Decorated with @abstractmethod
#   def draw(self):                     # defined a draw method and there is no implementation so just pass it
#     pass                              # This draw function is just for all derivatives in subclasss to must have

# class TextBox(UIControl):             # Created subclass and inheritated base class
#   def draw(self):                     # defined draw method and just print "TextBox"
#     print("TextBox")

# class DropdownList(UIControl):        # Created subclass and inheritated base class
#   def draw(self):                     # defined draw method and just print "DropdownList"
#     print("Dropdownlist")

# def draw(control):                    # defined draw function that takes UIControl object (control)
#   control.draw()                      # and draw() function in it


# ddl = DropdownList()                  # Created dropdownlist object, and pass the object to the draw() function
# # print(isinstance(ddl, UIControl))   # OutPut: True. this is to check the ddl is the instance of the uicontrol
# tb = TextBox()                        # Created tetbox object, and pass the object to the draw() function
# draw(ddl)                             # Output: Dropdownlist
# draw(tb)                              # OutPut: TextBox


''' Now we are making the codes little more interesting, instead of geting control(draw function) we want to a list
or tuple of controls(textbox, dropdownlist). So to do that we will run a for loop in draw function. Copping the codes
above and modifying at below; '''

from abc import ABC, abstractmethod       # import ABC class and abstract method from abc module


class UIControl(ABC):                 # Created a base class, and inheritated ABC class
  @abstractmethod                     # Decorated with @abstractmethod
  def draw(self):                     # defined a draw method and there is no implementation so just pass it
    pass                              # This draw function is just for all derivatives in subclasss to must have

class TextBox(UIControl):             # Created subclass and inheritated base class
  def draw(self):                     # defined draw method and just print "TextBox"
    print("TextBox")

class DropdownList(UIControl):        # Created subclass and inheritated base class
  def draw(self):                     # defined draw method and just print "DropdownList"
    print("Dropdownlist")

def draw(controls):                   # defined draw function that takes UIControl object (control)
  for control in controls:            # Run a for loop to get list of UIControls(dorpdowlist, textbox)
      control.draw()                  # and draw() function in it


ddl = DropdownList()                  # Created dropdownlist object, and pass the object to the draw() function
tb = TextBox()                        # Created tetbox object, and pass the object to the draw() function
draw([ddl, tb])                       # Output: Dropdownlist TextBox
