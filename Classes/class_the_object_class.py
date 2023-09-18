''' In Python, the object class is the base class for all classes. It is at the top of the class hierarchy
and serves as the parent for all user-defined and built-in classes. The object class provides some
fundamental methods and attributes that are inherited by all objects in Python. Here's a detailed
explanation of the object class with an example:

Methods Provided by the object Class:
__init__(self):
The __init__ method is called when an object is created from a class. It's the constructor method.
By default, the object class's __init__ method does nothing.

__str__(self):
The __str__ method is called by the str() function and when using print().
It should return a human-readable string representation of the object.
By default, the object class's __str__ method returns a string that includes the object's memory address.

__repr__(self):
The __repr__ method is called by the repr() function and is used for generating a string representation that, 
ideally, could be used to recreate the object. By default, the object class's __repr__ method returns a string
that includes the object's memory address.

__eq__(self, other):
The __eq__ method is called when using the == operator to compare objects.
By default, the object class's __eq__ method compares objects based on their memory addresses.

Example Using the object Class:
Let's create a simple class that inherits from object and overrides the __str__ and __repr__ methods to provide

custom string representations: '''

class MyObject(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyObject with value: {self.value}"

    def __repr__(self):
        return f"MyObject({self.value})"

# Creating instances of the MyObject class
obj1 = MyObject(42)
obj2 = MyObject(100)

# Using the custom __str__ and __repr__ methods
print(str(obj1))  # Output: MyObject with value: 42
print(repr(obj1))  # Output: MyObject(42)

# Comparing objects using the == operator
print(obj1 == obj2)  # Output: False (default behavior compares memory addresses)

''' In this example, we create a MyObject class that inherits from object.
We override the __str__ and __repr__ methods to provide custom string representations.
When we create instances of this class and use str() or repr(), we see our custom representations.
However, the default behavior of == still compares objects based on their memory addresses,
so obj1 == obj2 returns False. '''

''' Now if we use isinstance() builtin method and supplying obj1 instance and MyObject as parameter
and print. then we get boolean "True" because obj1 is the instance of MyObject class. 

Again if we use isinstance() method and supplying obj1 instance and object as parameter
and print. then we get boolean "True" again because obj1 is eventually the instance of object class.  '''

print(isinstance(obj1, MyObject))
print(isinstance(obj1, object))

''' Now if we define and create an empty object and use .dot oparator then we can see all the magic methods
that inheritated with object class. '''

o = object()
# o.

''' Now if we use the .dot oparator for obj1 we will see all the magaic methods as well because the obj1 is 
eventually inheritated with object class. '''

# obj1.

''' Another usefull built in method is issubclass() that shows if a class derived from another class. 
Here the base class is object and the MyObject class is the inheritance of object class, or a subclass 
of object class. '''
print(issubclass(MyObject, object))
