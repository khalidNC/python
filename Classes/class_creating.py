''' Creation a class start with 'class' keyword
then a class name with naming convension - first letter is capital and no underscore.
Then a colon(:) for next block on next line with indentation.
Then let's say we are defining a function draw() with parenthesis.
Now by convention we need write at least 1 parameter called self.
Then a colon(:) for next line block.
Let's just print something for this function, so this draw() function print something under the class Point.

So now we have a class or blue print for creating point object. So every objects we will create will have
the draw method. 
Let's have look; '''


class Point:
  def draw(self):
    print("Draw")

  
''' To create a class object we will call the class like a function by the name of the class.'''
# Point()
''' Now this will return the point object then we can assign a variable called point.'''
point = Point()

''' Now if we can use the dot(.) oparator like point. then we can see the draw funtion in the 
suggestion list along with others methods in a dropdown. Note: we are seeing the other methods because 
the python has other machanism called inheritence. '''
# point.

''' Now if we print the type of point. we get as output __main__.point 
the __main__ is a python module. '''
print(type(point))
#output: <class '__main__.Point'>

''' Another usefull method is isinstance() to check the instance/object is the instance of the class or not.
the syntax is, this method takes 2 arguments object name and class name.
isinstance(object_name, class_name) and it returns boolean True/False '''
print(isinstance(point, Point))
# Output: True

''' If we change the class_name for the 2nd argument then it will return False. '''
print(isinstance(point, int))
# Output: False
  

'''' This is how we can create custom class in python. 
Next, the Point calss need some initial values like x and y to set the value
we need constractor. That topic is covered in constractor.py file.'''
