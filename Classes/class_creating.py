''' Creation a class start with 'class' keyword
then a class name with naming convension - first letter is capital and no underscore.
Then a colon(:) fir next block on next line with indentation.
then a special method called constractor to initialize the class object parameter. 
Then other will write other functions for the class. '''

''' For example we are creating a class Point. 
then __init__ method to initialize class object atributes'''

class Point:
  def __init__(self, draw):
    self.draw = draw 

  def line(self):
    print(f"Line a to b {self.draw}")

  


  