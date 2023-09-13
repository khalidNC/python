''' There are times when we need to compair objects. '''


class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self):
    print(f"Point {self.x}, {self.y}")

  def __eq__(self, other):
    return self.x == other.x and self.y == other.y


point = Point(1, 2)
another = Point(1, 2)

print(point == another)
# Output: False

''' Here in this codes the output is "False" it is expaexted that this should be "True". 
This returns False because, the equal oparator(==) saves the references of the objects in the memory.
In thos case, the variables(point & another) references the 2 deferent objects in memory that's why 
it comes not equal. To fix this we can use the magic method. 

Go back to the link: https://rszalski.github.io/magicmethods/
and find the compairison object method: https://rszalski.github.io/magicmethods/#comparisons 

And define the magic method as line 12, 13 

Then the output comes to "True" '''
