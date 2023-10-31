''' A virtual environment in Python is a self-contained directory that houses a Python interpreter 
and its own set of libraries. It is used to isolate and manage Python packages and dependencies 
for different projects, ensuring that one project's dependencies do not interfere with another. 
Virtual environments are particularly useful when you have multiple Python projects with different 
library requirements. '''

''' To check the list of all installed packages we have we can use the command pip3 list this will
return the list of all the currently installed packages in the terminal;

We see requests 2.25.1 in the list that means we have already requests package installed and it's
main version is 2 and the minor version is 25 and the fix/patch 1.

Now let's say for another project we need the earlier version of request but the problem is we 
can not have different packages in our system side by side. To solved this problem we can create
an isolated vertual environment for each project and keep the dependencies in the virtual 
environment. 

So in the project directory we run the command to create virtual environment:

python -m venv name_of_directory that contains virtual environment by convention it is env
os it comes like; python -m venv env

But do not need to memorise this, there is a better and simple way to do this we will demo
that later.


'''

