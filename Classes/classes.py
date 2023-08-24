''' In Python, a class is a blueprint for creating objects (instances) that share 
the same attributes (variables) and behaviors (methods). Classes provide a way to 
define the structure and behavior of objects in an organized manner. 

Let's dive into the details of defining and using classes with examples. '''

# Defining a Class:
# You define a class using the class keyword. Here's a basic example of a Person class:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
