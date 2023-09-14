''' In the below codes if we want to add the 2 points line 26 and let's see what happens; '''


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self):
    print(f"Point {self.x}, {self.y}")

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __gt__(self, other):
    return self.x > other.x and self.y > other.y
  
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)


point = Point(4, 6)
another = Point(1, 2)
combine = point + another

print(point == another)
# Output: False

print(point > another)
# Output: True

print(point + another)
# output: TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

print(combine.x)
# Output: 5 

''' Now we use __add__(), one of numeric magic methods in line. Now we get 
output: __main__.Point object at 0x10febbe20 that mean we get new point object in this memory address. 
and we do not see the actual value of x, y. Hoewever, if we store the resulst in a new object combine(see line 24) 
then print the x, y value then we can see actual values of x, y'''
