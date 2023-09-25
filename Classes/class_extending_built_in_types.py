''' In Python we can also use built-in inheritance. For example, we created a class Text with str built-in 
inheritance. Here, the Text class will inheritate all the features(methods) of built-in base class str. We can also
add new feature(function) to the Text class by define new function, for example here we add new function duplicate. '''


class Text(str):
  def duplicate(self):
    return self + self
  
text = Text("Python")
print(text.lower())
print(text.duplicate())


class TraceableList(list):
  def append(self, object):
      print("Append called")
      super().append(object)
     

my_list = TraceableList()
my_list.append("1")

print(my_list)


''' let's break down both examples step by step:
1. You define a new class called Text that inherits from the built-in str class. This means that Text inherits 
   all the methods and behavior of str.

2. Inside the Text class, you add a custom method called duplicate which takes the current text and returns it 
   concatenated with itself.

3. You create an instance of the Text class called text with the content "Python".

4. When you call text.lower(), it's using the lower method inherited from the str class to convert the text 
   to lowercase, resulting in "python."

5. When you call text.duplicate(), it's using the custom duplicate method defined in the Text class, which duplicates 
the text and returns "PythonPython". 

6. In 2nd example, You define a new class called TraceableList that inherits from the built-in list class. 
This means that TraceableList inherits all the methods and behavior of list.

7. Inside the TraceableList class, you override the append method. This overridden append method first prints 
"Append called" and then calls the append method of the superclass using super().append(object) to ensure that 
the object is added to the list as usual.

8. You create an instance of the TraceableList class called my_list.

9. When you call my_list.append("1"), it calls the custom append method defined in the TraceableList class, 
which prints "Append called" and then appends the string "1" to the list.

10. So, if you print my_list, it should display: ['1'] 

It's important to note that in the second example, you've overridden the append method of the list class to add 
a custom behavior (printing "Append called"). This is an example of method overriding and extending the behavior 
of a built-in class. '''
