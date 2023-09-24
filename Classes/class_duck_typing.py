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

# def draw(controls):                   # defined draw function that takes UIControl object (control)
#   for control in controls:            # Run a for loop to get list of UIControls(dorpdowlist, textbox)
#       control.draw()                  # and draw() function in it


# ddl = DropdownList()                  # Created dropdownlist object, and pass the object to the draw() function
# tb = TextBox()                        # Created tetbox object, and pass the object to the draw() function
# draw([ddl, tb])                       # Output: Dropdownlist TextBox

''' The above codes is the classic example of achiving polymorphism. But Python is a dinamic language it can still 
achive the same polymorphic results without the abstract base class. Let's say at the above codes if we remove 
the abstract base class and the inheritance still the codes achive the same results becuse Python support duck typing.
It is because the python interpreter concern is not the type of object of the class, it concerns as long as the method 
and object is present. So any type of objects like list, tuple, str etc we can pass in the draw() mehod and the Python
interpreter understands this is the object of all UIControls(TextBox, DropdownList etc) classes. And this is called 
duck typing. Let's try it out below: 

But still it is a good practice to define the abstract base class because it make the method as a common interface. '''

class TextBox():             
  def draw(self):                    
    print("TextBox")

class DropdownList():        
  def draw(self):                     
    print("Dropdownlist")

def draw(controls):
  for control in controls:
      control.draw()


ddl = DropdownList()
tb = TextBox()
draw([ddl, tb])
