''' Magic methods in Python, also known as dunder methods (short for "double underscore" methods), 
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
