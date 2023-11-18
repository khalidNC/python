import math
from khalidpdf import pdf2text


math.floor()

pdf2text.convert()


'''
Docstring:
The package we uploads on pypi should be well documented so that other people knwo how to use it.
For example think about math module. We import the math module and then call any of it's methods
then keep the cursor on the method and a popup text with little description appears as below;

(function)
def floor(
    __x: _SupportsFloor[_T@floor],
    /
) -> _T@floor: ...
def floor(
    __x: _SupportsFloatOrIndex,
    /
) -> int: ...
Return the floor of x as an Integral.

This is the largest integer <= x.

It is called intellicense. Vscode has this feature that read the documentation of this method and
display in a popup window. 

In contrust our convert function(that we did in separate project called 'khalidpdf') has no documentation.
So if we call the method here on the top it is not clear how to use the method.

This is a basic function but in a real application we could have a function with one or more parameters so
people who use this function need to konw;
                                          - What these parameters are
                                          - What this function does
                                          - What it returns

So this is the prupose of the documentation. In python we have special format of documenting codes called
docstring or documentation string. This is basically a string with triple quotes that we add right after
the declaration of a function or class or variable. 

This is different that comments(#) because comments we use to explain why have we done this in a certain way.
So we should not use a comment to explain what a function does. What it does should be refeclated in the 
documentation string. What is does, how it does and why we implemented in a certain way should come in a 
comment.  

So let's discuse how we should document this khalidpdf package-functions using docstring;

When we publish a module for other people to use, we should document the module itself as wel as every
object in it. So any classes or any method in those classes, or any stand alone function in those modules
should be perfectly documented. 

1. Document the modlue:
   In the first line start with triple quotes and """ One line description. """ ends with triple quotes.
2. Document the function:
   If you want to explain more you can use multiple lines like
   """
   First line should be short summery. 

   Then a balnk line, than more detailed explanation.
   """
3. For example in khalidpdf module:
   a. Document the moduel with one line with in tripple quote at the top.
      """ This module provides function to convert a PDF to text. """

   b. Document the function with first line short summery just under the line def.
      Then a blank line. Then parameters, need to specify what the parameter is, what the type is,
      and what we use for it.
      let's give a parameter path
      type of the parameter path, (str)
      Now if we have more parameter then we need to list them in each line.
      Then we need a blank line
      Then we need to specify what the function returns:

      def convert(path):
      """ 
      Convert the given PDF to text.
      
      Parameters:
      path (str): A path to a PDF file

      Returns: 
      Str: Then content of the PDF file as text 
      """
      print("pdf2text")

4. Now to demonastrate what the consumers of this module will see. Let's create a python file in the root 
   directory name it let's say app.py 
   then import the pdf2text module from khalidpdf.
   Then place the cursor on pdf2text  then you can see the documentation you just did as below in a pop
   up window:
    (module) pdf2text
    This module provides function to convert a PDF to text.

  Then call the pdf2text method and you can see the documantation in a popup window as below:

    (function) def convert() -> None
    Convert the given PDF to text.

    Parameters:
    path (str): A path to a PDF file

    Returns:
    Str: Then content of the PDF file as text

5. Now go back to the project khalidpdf. Here is only a function but if there is a class. Then 
   we need to document the class as well. As an example we difine a class on pdf2text file.
   a. difene the class: class Converter
   b. put the converter() method inside the class by 2space indentation
   c. Then need to add first parameter self
   d. Right after the class declaration add triple quotes and sumerize the behabiour of this 
      class. 
   
   Finally, it looks like this:

    class Converter:
      """ A simple converter for converting PDFs to text. """

      def convert(self, path):
        """ 
        Convert the given PDF to text.
        
        Parameters:
        path (str): A path to a PDF file

        Returns: 
        Str: Then content of the PDF file as text 
        """
        print("pdf2text")

This is the basic of documenting the module with docstring. '''
