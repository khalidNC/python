''' 
Pydoc:
Pydoc is a python utility that comes with python instalation. With this utility you can easily see
the documentation for a module. That module can be one of the modules in Python standard library or
one of our own modules. Let's us show;

in the terminal on mac run the command: pydoc3 then_the_module_name

For example: pydoc3 math

Output:
Help on module math:

NAME
    math

MODULE REFERENCE
    https://docs.python.org/3.10/library/math.html
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

:

Upto the colon(:) mark is first page. To go to the next page hit Space bar in the keyboard. Or you can
just scroll up. 

When you come to the edn of the page it seems like this:

FILE
    /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload/math.cpython-310-darwin.so

(END)

Then hit q in the keyboard and you are out of the pydoc.

Now we are going to see the documentation of our own module:

Terminal command: 
First active the virtual environment: pipenv shell
Then run this command: pydoc khalidpdf.pdf2text

Output:
Help on module khalidpdf.pdf2text in khalidpdf:

NAME
    khalidpdf.pdf2text - This module provides function to convert a PDF to text.

FUNCTIONS
    convert(self, path)
        Convert the given PDF to text.
        
        Parameters:
        path (str): A path to a PDF file
        
        Returns: 
        Str: Then content of the PDF file as text

FILE
    /Users/user/.local/share/virtualenvs/Python_Course-Tq5mYnnj/lib/python3.10/site-packages/khalidpdf/pdf2text.py

(END)

Now pydoc has few interesting switches, one of them is 'w' for writing this docuemntation to an html file.
To do so run this command:

pydoc -w khalidpdf.pdf2text

Output:
wrote khalidpdf.pdf2text.html

This actually generated an html file for the module in th root directory

Now to open the file run the command: open khalidpdf.pdf2text.html

This open the html in a web browser.

Pydoc has another interesting switch to open this documantation as well as python standard library in a 
locally hosted web server.

To do so run this command: pydoc3 -p (short from of port) then port number like 1234

Since we installed the twine package in our virtual environment for the project.
So we actually activate the virtual environment first.
then run the command:

pydoc -p 1234

Now the server is ready at http://localhost:1234/
Server commands: [b]rowser, [q]uit
server> b

Open the server in a browser window. 
Here we can see the package khalidpdf under:
/Users/user/.local/share/virtualenvs/Python_Course-Tq5mYnnj/lib/python3.10/site-packages

If we click on the package it takes me to the inside and we can see the package contents
pdf2text and pdf2 image
then go to pdf2text and here we can see the documentation that we wrote.

Aslo we can see the python standard library here. 
'''
