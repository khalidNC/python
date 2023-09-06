''' Instance Attributes: '''

class Point:
  def __init__(self, x, y):       # This is constructor of Point class
    self.x = x                    #These 2 are attributes of Point object(line 9)
    self.y = y

  def draw(self):
    print(f"Point {self.x} and {self.y}")

point = Point(1, 2)               # Class object
point.z = 4                       # Attributes are dynamic in python like JS so we do not always define in constructor
point.draw()

''' Now whenever we create new point object this point object will have these atributes by default.
We can also define new attribute after we create point object. line- 10 
Note: all the attributes here we added are the instance attributes. In other words, these attributes
are belong to the point instance or point object. So every point object has different value for these
attributes. 

Here is an example: we added another object with different value. then call the draw function.
and get different values. '''

another = Point(5, 6)
another.draw()
# Output: Point 5 and 6


''' Class attributes: 

Above are the examples of instance arrtibutes we can also define attributes in class lavel and the class
attributes are the same accrose all instances of a class. 

As a metafore we can say, all human has 2 eyes adn 2 ears so these are the attributes we define a class level
and they are shared with all instances. Let's write a similer class at below and add a class attributes. '''


class Human:
  default_org = "Nose"                            # We added a class level attribute syntax: variable = data_type

  def __init__(self, eyes, ears, name):
    self.eyes = eyes
    self.ears = ears
    self.name = name

  def human_function(self):
    print(f"{self.name} has {self.eyes} eyes and {self.ears} ears")

khalid = Human(2, 2, "Khalid")
nameera = Human(1, 2, "Nameera")
print(nameera.default_org)                 # Then we can call the class attribute in object level: Output: Nose
print(Human.default_org)                   # Also we can call the class attribute in class level: Output: Nose
nameera.human_function()
khalid.human_function()
