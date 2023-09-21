''' Let's say we data stream and we read data from file, network and other sources. So there are things like,
opening a file, closing a file are same functions and read from the file and read from network 
is different. so we can create a base class Stream and function for open and close and use the class as inhertance 
in subclasses to read from file and network. '''

class InvalidOparationError(Exception):
  pass

class Stream:
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

class FileStream(Stream):
  def read(self):
    print("Read data from a file")

class NetworkStream(Stream):
  def read(self):
    print("Read data from a network")


read_from_file = FileStream()
read_from_network = NetworkStream()
read_from_file.read()
read_from_network.read()

''' Code break down step by step:
1. Created a base class Stream
2. Define a method open(). And it's function is to open, so just set self.open equal True.
   But what if, the data source is already opened? 
3. So let's create a constractor and initialize the open option euqal False. Means initially it is closed.
4. Now check the data source is already opened if oppoend then raise an exception. So if self.opened: raise 
5. We need to rasie an exception, but what type of exception it is? In python there is no exception error for
   the open, so we need to create a custom exception error.
6. Custom exception error creation syntax is, class NameOfTheError(Exception): then pass 
   Note: the nameing convention is the last word must be Error, and have to inherite base class Exception. 
7. Now raise exception and write a message "The stream is already opended". 
8. Then define a function close() and make it self.open equal False, means this function closed the data source.
9. And in same way raise an exception if the data source is already closed. 
10.Create two classes FileStream & NenworkStream and define function to read data just a print command as output.
11.Now inherite the stream class, and create instance read_from_file & read_from_network then call the function. '''
