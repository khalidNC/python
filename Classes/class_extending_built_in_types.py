''' In Python we can also use built-in inheritance. For example, we created a class Text with str built-in 
inheritance. Here, the Text class will inheritate all the features(methods) of built-in base class str. We can also
add new feature(function) to the Text class by define new function, for example here we add new function duplicate. '''


class Text(str):
  def duplicate(self):
    return self + self                       # This function make the parameter dup;icate and returns
  
text = Text("Python")
print(text.lower())                          # Here text. can access all the methos of str class. e.g we use lower()
# Output: python
print(text.duplicate())                      # Also we can use the custom method duplicate()
# Output: PythonPython

''' Another example, we can use built-in list class. '''

class TraceableList(list):                  # Created a class and inheritated list class
  def append(self, object):                 # Then override the append() method
      print("Append called")                # Print a message after append item in list
      super().append(object)                # Then just call the append base class syntax(super().append(supply object))
     

list = TraceableList()                     # Created an object   
list.append("1")                           # call the append method for the list object
# Output: Append called
