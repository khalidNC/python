''' The class is extremly important in Python or programming in general.
Let's have some examples: '''

# We are defining a list of numbers
numbers = [1, 2]
# Then when we use dot notation we can see set of methods for the list
numbers.clear()
print(numbers)

# Now if we create objects like;
shopping_cart = []
shopping_cart.add()
shopping_cart.remove()
shopping_cart.get_total()

''' Defining a Class:
You define a class using the class keyword. Here's a basic example of a Person class: '''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

''' In this example, we've defined a class called Person with two attributes (name and age) and a method (greet).
The __init__ method is a special method called a constructor. It initializes the object's attributes when an object 
is created. The self parameter refers to the object being created. The greet method is a simple method that prints 
out a greeting using the object's attributes. '''

''' Creating Objects:
Once you have a class, you can create objects (instances) of that class. Here's how you do it: '''

