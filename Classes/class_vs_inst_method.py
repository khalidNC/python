''' Instance method:
The below codes, the both methods we have defined in Point class are instance methods. 
So we can call them using the instance of the point class using an object.
In general speaking, use this instance method whenever we need an object reference. 
For example, to konw the human_function you really need specific objects. This is why 
the human_function method here is a instance method. '''


class Human:

  def __init__(self, eyes, ears, name):
    self.eyes = eyes
    self.ears = ears
    self.name = name

  def human_function(self):
    print(f"{self.name} has {self.eyes} eyes and {self.ears} ears")

khalid = Human(2, 2, "Khalid")
nameera = Human(1, 2, "Nameera")

nameera.human_function()
khalid.human_function()


''' Class method:
There are times that you do not really need the existing object and then we use class method.
For example, in the below codes, sometimes we may set the initial value (0, 0) for the object(line 69)
This is one way to create point object.
We can come up with a different way to create point object with the value(0, 0) like this:
line 70: Point.zero() note that we are using the class reference here. In this case, the zero()
is the method that defined as class level and when we call it, it returns the point object 
with initialize the value zero. Now can just assing this in point variable. 

Now in this example we reffer this zero method as a factory method. Because its like a factory to create 
new object.

The object with this zero value is very basic here are times we may need to pass other values like; int, str 
point = Point(0, 0, 1, "a") and may repete this in several places. 

In that case, instead of passing all the magical value, we can use the factory method that return an object with 
the desire value to avoid this complexity.

Now let's see how we can define the factory method in class level. 
syntax: def zero(cls): [Note: the first parametre is by convention 'cls' that refer class ]
now to make this method as class method we need to decorate this @classmethod(this is called decorator)
like; line 61-63
@classmethod
def zero(cls):
    return cls(0, 0)
now create point object with initial value(0, 0) and return it 
'''


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  @classmethod
  def zero(cls):
    return cls(0, 0)

  def draw(self):
    print(f"Point {self.x}, {self.y}")

# point = Point(1, 3)
# point = Point(0, 0)
point = Point.zero()

point.draw()
#Output: Point 0, 0
