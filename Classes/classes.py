''' The class is extremly important in Python or programming in general.
Let's have some examples: '''

# We are defining a list of numbers
numbers = [1, 2]
# Then when we use dot notation we can see set of methods for the list
numbers.clear()
print(numbers)

# Now if we create objects like;
# shopping_cart = []
# shopping_cart.add()
# shopping_cart.remove()
# shopping_cart.get_total()

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

person1 = Person("Khalid", 42)
person2 = Person("Borna", 38)


''' Here, we've created two Person objects, person1 and person2, with different names and ages.
Accessing Attributes and Methods:
You can access an object's attributes and methods using the dot notation '''

print(person1.name)  # Output: Khalid
print(person2.age)   # Output: 38

person1.greet()      # Output: Hello, my name is Khalid and I am 42 years old.
person2.greet()      # Output: Hello, my name is Borna and I am 38 years old.


''' Inheritance:
Classes can also inherit attributes and methods from other classes. This allows you to create a new
class based on an existing class, adding or modifying functionality. Here's a simple example of inheritance: '''

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} student id {self.student_id}, is studying {subject}")

student1 = Student("Nameera", 9, "S12345")
student1.greet()     # Output: Hello, my name is Nameera and I am 9 years old.
student1.study("Math")  # Output: Nameera is studying Math and her student id is S12345
