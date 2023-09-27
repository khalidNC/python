import mymodule
import sys

print(sys.path)

''' Let's we import mymodule module. Now python will look at mymodule.py file. If it does not find the module 
then python will look around other pre-define directories that come with python installation. Let's check it out.
we have built-in module called sys let's improt it. In  tghis module there is a variable called path which returns
list of directories where Python actually looks at for the finding the module. 

Now print the path and see the resutls, 
Output: 
['/Users/user/Desktop/Python Course/Modules', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python310.zip', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload', 
'/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages'] 

It returns the list of all directories path in string. The first element represent the current directory in my machine.
After that we have library/framework ... it differs machine to machine. Since we are using mac and the path address
looks like this. 

So when we inport mymodule python will look at all this directories to find the module. As soon as it find the module
the search stops. '''

''' Now there might be a question how would we search module from sub-directory. Let's check it out in module_packages.py
file. '''
