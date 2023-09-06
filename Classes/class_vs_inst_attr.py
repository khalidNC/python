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
