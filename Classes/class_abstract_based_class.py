from abc import ABC, abstractmethod

class InvalidOparationError(Exception):
  pass

class Stream(ABC):
  def __init__(self):
    self.opened = False

  def open(self):
    if self.opened:
      raise InvalidOparationError("The stream is already opended")
    self.opened = True

  def close(self):
    if not self.opened:
      raise InvalidOparationError("The stream is already closed")
    self.opened = False
  
  @abstractmethod
  def read(self):
    pass

class FileStream(Stream):
  def read(self):
    print("Read data from a file")

class NetworkStream(Stream):
  def read(self):
    print("Read data from a network")

class MemoryStream:
  def read(self):
    print("Read from memory" )


# streams = Stream()
# print(streams.open())

streams = MemoryStream()
streams.read()

''' In general, Through the process of abstraction, a programmer hides all but the relevant data about an object
in order to reduce complexity and increase efficiency. On the above example of inheritance class has a couple of
issues;
1. If I wish I can create instance on base class and call it's function. and the program runs. Line-37, 38 
   here the issue is, when I call open() function what I actually open? So the correct approch is to create sub-
   class's instance. 
   
2. If we look at the impelementation of the sub-classes FileStream, and NetworkStream we see both clasess have read()
   function. And if in future, we add another type of stream then we have to remember the read() method and 
   exactly called read() method we might define method read_line() or read_str() and whatever the name
   but this is not consistance behaviour. In other words, currently there is no way to enforce the common interface 
   accross the different type of streams. 
   
So how can we solve this problem? That's when we use the abstract base class. The abstract base class is like a half
baked cookies, it not ready to be eatten. It's purpose to provide the common codes. So here we will make the Stream
class an abstract class. 
To do that we will go to top of the page and import ABC class and abstractmethod(we use this
as decorator) from abc module. Note: the module name is all lowercase 'abc' and the class name all cap 'ABC'. 

Now 
The first step: we will inherite ABC class in stream class. class Stream(ABC)
The second step: need to define a common enterface for all streams, in other words, all streams have read() method. 
                 So we define a read() method in Stream class. See line-21. There is no emplementation so just pass.
The third step: Now we need to decorate this method with @abstractmethod. line 20 '''

''' This abstract implementation solved the both issues. Like if we run the program now we will see TypeError.
Output: TypeError: Can't instantiate abstract class Stream with abstract method read 
It's mean when a class has an abstract method it consider as abstract class and we can not instantiate, which means 
we can not create instance.

Secondly, future if we create another stream class MemoryStream and just pass(line-32, 33). It still does not allow me to run the 
codes, it gives TypeError. Because, if we look at the abstractmethod(line-20, 21, 22) here read method is define, so
till we use the read() method for all type of Stream class it will keep raising error. '''