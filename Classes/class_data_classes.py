from collections import namedtuple


''' In larger program we might have dealing with classes that do not have any method only data. 
Here is an example:

1. Created Point class
2. Initialized with 2 attributes and the class have no method only data. 
3. Created 2 Point object p1, p2 with same x, y value 1, 2
4. When we compaire this 2 point object == and print the results it returns False. It is because 
   the objects stored in a different locations in the memory. By default Python compaires objects based on 
   where they are located in the memory. So it returns Flase. 2 variables are referencing the object in the same 
   memory location they are considered equal. In this example, the their memory location is different even though 
   their values are same. We can check this with biult-in method id(). 
5. To solve this comparing issue with objects, we need to define a magic method __eq__ and return the comparison 
   self.x equal other.x now if we run the program this time it returns True. '''

# class Point:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

#   def __eq__(self, other):
#     return self.x == other.x and self.y == other.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)
# # print(id(p1))     # Output: 4358372176
# # print(id(p2))     # Output: 4359852656
# print(p1 == p2)

''' However this codes do not have any method it has just data. If you are dealing with classes that do not
have behaviour only data then you can use namedtuple instance. Let's see how works that, 
1. First, on the top we import namedtuple function from collections module
2. Then define the namedtuple class instead the regular defining class in this case Point. 
   The syntax of defining namedtuple class is, NamedTupleClass = namedtuple('TypeName', ['field1', 'field2', ...])
   a. NamedTupleClass: This is the name of the class that represents the named tuple.
   b. TypeName: This is a string that specifies the name of the named tuple type.
   c. ['field1', 'field2', ...]: This is a list of field names that define the structure of the named tuple. 
      Each field name is a string. These are the attributes in comparison to class initialization.
  Once you've defined a named tuple class, you can create instances of it, access fields using dot notation or indexing,
  and take advantage of the immutability and named fields that named tuples offer. 
3. Here we use keyword argument thate makes the codes more clear.
4. So this returns True. And here we do not need the magic method __eq__ anymore.

So when there is only data in the class we can use namedtuple instead regular class. 
Couple of things to be noted:

1. We can print attribute like. print(p1.x)
2. This named tuple is immutable. Means, we can not change or modify the value of x, y after creating it. like, if we 
   set p1.x = 10 in line-60 and run the program it gets AttributeError: can't set attribute 
3. But if you really need to change the vlaue then you need to create a new Point object. p1 = Point(x=10, y=2) '''


Point = namedtuple("Point", ['x', 'y'])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
# p1.x = 10
# p1 = Point(x=10, y=2)
print(p1 == p2)
# Output: True.

''' Here is another example: 

In Python, the namedtuple function from the collections module is used to create simple, immutable, 
and named tuple-like objects. Named tuples are similar to regular tuples but have named fields that can be 
accessed using dot notation (e.g., person.name, person.age) instead of indexing (e.g., person[0], person[1]). 
Here's how you can use the namedtuple function: '''

from collections import namedtuple

# Define a named tuple class
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances of the named tuple
person1 = Person('Alice', 30, 'New York')
person2 = Person('Bob', 25, 'San Francisco')

# Access fields using dot notation
print(person1.name)  # Output: Alice
print(person2.age)   # Output: 25
print(person1.city)  # Output: New York

# You can also access fields using indexing (like a regular tuple)
print(person1[0])    # Output: Alice
print(person2[1])    # Output: 25
