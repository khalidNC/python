''' In the point object we give the initial value for x, y. '''


# class Point:
#   def draw(self):
#     print("Draw")

# point = Point(3, 4)


''' Now to achive this this we need constructor, which is a special method syntax: 
def __init__(self, optional_parameter) first define a function under the class then 
double underscore then init then double underscore then parenthesis and by convension 
1 parameter 'self' then optional parameter. '''

''' Self - self is a reference of current class object which is 'point' here. So here 
in the line 27, the python interpreter store the point objet Point(3, 4) in memory and 
set the self as reference to the object. 

Now the point object has a bunch of methods like if we use the dot(.) oparator point.
we can the list of methods for the point object. 

Then the object also have atributes, which are basically the variables that has data 
about the object. For an example, we have atribute x and we can print the value of 
print(point.x) in terminal. 

In other words, the class bundle the data and function related to that data into one unit.
Once again, as a metafore think of a human, a humam has atributes like age, hight, color and so on 
as well as functions walk, talk etc. '''

''' Now back to the constructor, self is the reference of current object now we can can use that
to set atributes syntax self.x = 0 or x we can either set the default vale zero or the x argument that
receive the value.  '''

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self):
    print("Draw")

point = Point(3, 4)
''' Now if we use dot(.) oparator point. then we can see draw() method as well as x, and y tributes.
And now we can print the value of x '''
print(point.x)
# Output: 3


''' Now take a look at the actual funtion draw the self here, is reference to the point object so we can 
easily print the value of the atributes x, and y in the draw function. '''

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def draw(self):
    print(f"Point {self.x} and {self.y}") #we use formater and print the value of x, and y

point = Point(3, 4)

''' Now sempilly call the function by point.draw(). And get the result of the draw function. Here,
the draw function work is to print the value of the atributes. '''
point.draw()
#Output: Point 3 and 4

''' Here the noticeable things is, when we call the draw() method we do not supply the value of the self
parameter as argument in the parenthesis line 67. Because Pthon does that by default. '''

''' So the take away is:
1. The method we define in a class have at least 1 parameter which by convention is called 'self' 
2. And the self is the referenc to the currect object that we are working with
3. When calling the metghod of an object never need to supply the value for the self parameter because 
python interpreter does that for us. '''
