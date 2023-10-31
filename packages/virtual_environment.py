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
os it comes like; python3 -m venv env

But do not need to memorise this, there is a better and simple way to do this we will demo
that later.

After run this command I noticed env directory has been created in the current project directory. 

Here in the env directory we see, pyvenv.cfg configuire file. In this file, we see home is reffer to 
this path directory /usr/local/bin where the python interpretor and version 3.10.0 is installed. 
We also have bin, the binary directory contains lots of tools like pip, pip3, python, python3 etc.
And inside lib directory, we have python3.10 and inside site-packages. 

Now we have the virtual environment and we need to activate it now. In bin directory there is a 
active script we need to run this from the terminal. 

The run command for mac is, source env/bin/activate
So let's run it.

After we run this we see the terminal line is; (env) USERs-MacBook-Air:Python Course Khalid$
So we are in the virtual environment.

Now let's install an earlier version of requests 2.9.* which is different than 2.25.1 which
is installed in our local. 

so we run this command: pip3 install requests==2.9.*

So it has installed succesfully and the outcome as below:
Collecting requests==2.9.*
  Downloading requests-2.9.2-py2.py3-none-any.whl (502 kB)
     |████████████████████████████████| 502 kB 707 kB/s 
Installing collected packages: requests
Successfully installed requests-2.9.2

So this requests is spesifically for this enviroment and for this project.

Now on site-packge directory requests folder appears. Here the requests 2.9.2 has installed.

After this done command deactivate
It deactivate the virtual environment. '''
