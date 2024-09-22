'''
Magic methods in Python, also known as dunder methods (short for "double underscore" methods), 
are special methods that have double underscores at the beginning and end of their names, 
like __init__, __str__, __add__, etc. These methods are used to define how objects of a class 
behave in various contexts. They enable you to customize the behavior of your classes and objects 
in a way that makes your code more readable and Pythonic. 

Here are some commonly used magic methods and their purposes:

__init__(self, ...):
The constructor method is called when an object is created from a class. It initializes the object's attributes.
Example: def __init__(self, name, age):

__str__(self):
The str method is called by the str() built-in function and when using print(). It should return a human-readable 
string representation of the object.
Example: def __str__(self): return f"{self.name}, {self.age} years old"

__repr__(self):
The repr method is called by the repr() built-in function and can be used for generating a string representation that, 
ideally, could be used to recreate the object.
Example: def __repr__(self): return f"Person('{self.name}', {self.age})"

__len__(self):
The len method is called by the len() built-in function and should return the length of the object, typically for 
collections like lists or dictionaries.
Example: def __len__(self): return len(self.data)

__add__(self, other):
The add method is called when the + operator is used with objects of the class. It defines how two objects should be 
added together.
Example: def __add__(self, other): return self.value + other.value

__sub__(self, other):
Similar to __add__, but for the subtraction operator -.
Example: def __sub__(self, other): return self.value - other.value

__eq__(self, other):
The equality method is called when using == to compare objects. It defines how object equality is determined.
Example: def __eq__(self, other): return self.name == other.name

__lt__(self, other), __le__(self, other), __gt__(self, other), __ge__(self, other):
These methods are used to define comparison operators (<, <=, >, >=) between objects.
Example: def __lt__(self, other): return self.age < other.age

__getitem__(self, key), __setitem__(self, key, value), __delitem__(self, key):
These methods allow you to define custom behavior for accessing, setting, and deleting items in an object, 
similar to dictionaries.
Example: def __getitem__(self, key): return self.data[key]

__iter__(self), __next__(self):
These methods enable you to create iterable objects with custom iteration behavior.
Example: Implementing a custom iterator.

These are just a few examples of the many magic methods available in Python. By implementing these methods 
in your classes, you can control how objects of those classes interact with Python's built-in functions and 
operators, making your code more expressive and powerful. '''


''' The __init__ method in Python is a special method, also known as a constructor, used for initializing 
the attributes (properties or variables) of an object when it is created from a class. The __init__ method 
is automatically called when you create a new instance (object) of a class. Here's a more detailed explanation 
of the __init__ method:

Method Name: The __init__ method is always named __init__, and it must have at least one parameter: self. 
This is a reference to the instance of the object being created and is required in every instance method within 
a class.

Parameters: Besides self, you can define additional parameters for the __init__ method. These parameters are used 
to initialize the attributes of the object. For example: '''

class MyClass:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2

''' In this example, param1 and param2 are parameters for the __init__ method, and they are used to initialize 
attribute1 and attribute2. Attribute Initialization: Inside the __init__ method, you typically set the initial 
values of the object's attributes using the self reference. This allows each instance of the class to have its 
own unique set of attributes.

Automatic Invocation: When you create an object from the class, Python automatically calls the __init__ method 
with the parameters you provide during object creation. For example: '''

my_object = MyClass("value1", "value2")

''' Here, "value1" and "value2" are passed as arguments to the __init__ method, and they initialize attribute1 
and attribute2 for the my_object instance.

Instance Attributes: After the object is created, you can access its attributes using dot notation. For instance: '''

print(my_object.attribute1)  # Output: value1
print(my_object.attribute2)  # Output: value2

''' Multiple Instances: You can create multiple instances of the same class, and each instance can have its own set 
of attribute values. The __init__ method is crucial for defining the initial state of objects and ensuring that objects 
of a class have the required data when they are created. It's a fundamental part of object-oriented programming in 
Python and is used to construct objects with specific characteristics and behaviors. '''

''' We can find more deatil about magic method here: https://rszalski.github.io/magicmethods/'''
