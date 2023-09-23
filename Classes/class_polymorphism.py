''' Polymorphism is a fundamental concept in object-oriented programming that allows objects 
of different classes to be treated as objects of a common superclass. It promotes flexibility, 
code reuse, and the ability to work with different types of objects in a uniform way. In Python, 
polymorphism is achieved through method overriding and duck typing. Here's an explanation of 
polymorphism in Python: '''

from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self):
    self.sound = []

  @abstractmethod
  def speak(self):
    pass

class Dog(Animal):
  def speak(self):
    return "woof!"
  
class Cat(Animal):
  def speak(self):
    return "meow"
  
def animal_sound(animals):
    sounds = []
    for animal in animals:
      sound = animal.speak()
      sounds.append(sound)
    return sounds

dog = Dog()
cat = Cat()
print(animal_sound([dog, cat]))