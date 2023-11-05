''' So far we know to use pip and know how to create virtual environment. 
And all the terminal command we need memorise there are lot's of things we momorise 
to make our life easy pipenv comes into the picture. This pipenv is a tool that 
combines both needs together. So we do not have to use pip and vertual environment
separately. It is a dependescy manager in python pacakages. 

So let's use pipenv. First we need to install pipenv. So write and run this command in 
terminal; 
1. pip install pipenv --user : Doc link: https://pipenv.pypa.io/en/latest/installation/
2. After pipenv installed, we need to set path variable in .bash_profile
3. To set path need to to do below steps:
    a. Open terminal and go to home directory
    b. Check the .bash_profile file is already created. Terminal commad: ls -al
    c. Also can check in user folder: shift+comand+dot this will display all hidden files
    d. If the file is not there then create: terminal command nano .bash_profile
          i. This will open the bash_profile file in nano text editor
          ii. Then export the path, the syntax is: export PATH="actual/path:$PATH"
          iii. Then save the file shortcut key: control+o then hit Enter
          iv. Then exit shortcut: control+x
    e. We can also create and export path in text editor: terminal command: open .bash_profile
          i. To create bash_profile: touch .bash_profile
          ii. Open the file in text editor: open .bash_profile
          iii. Then export PATH="path:$PATH", then just save the file by using: command+s
    f. After creating and export PATH, we need to source the file.
          i. To do so the terminal command: source ./.bash_profile
          ii. Then restart the terminal and check pipenv command like: pipenv --version
4. Now, the way to find the actual path the terminal command: python3 -m site --user-base or -site
    a. This returns the user PATH like: /Users/user/Library/Python/3.10 and -site returns site-packages path

5. After doing those as above we should see the pipenv command work in terminal. 
    a. Like, pipenv --version command returns the version in the terminal
    b. Now we actually not need virtual environment(the env) folder that we created before. So we delete this.
       Because we do not need this anymore since we will use pipenv and this will create virtual env automatically.
       The pipenv allows both, creating virtual environment and installing packages.
 
6. Now we can install the dependency packages through pipenv instead pip3 the commad like, pipenv install requests
    a. This will install request for the project specially not for global.
    b. And automatically created a couple of files: Pipfile, and Pipfile.lock
    c. Also it creates an virtual environment for us and installed the requests package inside the environment.
    d. But the vertual envornment is not visible inside the project directory. Let's where is it;
            i. Run this command line in the terminal: pipenv --venv
            ii. This will return the path of the virtual environment directory: 
                  /Users/user/.local/share/virtualenvs/Python_Course-DQXbx9fU
            iii. We can see this directory is not the part of our project but this is a deliberate decision
                  and the main reason behind this, we may installed tons of packages and dependencies for the 
                  project and this increase the size of the project. So we want to exclude the virtual env
                  from our project directory. 
                  
7. To show how the requests package works that we installed in the vertual environment, we are deleting 
   the global one that we installed through pip3. So run the command: pip3 uninstall requests 
   
   Now if we run the program file pip.py we will get error that requests module not found because we 
   deleted this. And here Python has no idea where the vertual environment and the requests module is
   located. So we need to activate the environment.
   
   Do to so run the command: pipenv shell this activate the environment. And we will see in the terminal:
   Launching subshell in virtual environment...
   USERs-MacBook-Air:python course Khalid$  . /Users/user/.local/share/virtualenvs/Python_Course-DQXbx9fU/bin/activate
   (Python Course) USERs-MacBook-Air:python course Khalid$  
   
   Now if we run the program file pip.py once more time this time it works. 

8. we are in the virtual environment so if we want to deactivate the env then simply type exit in the 
   termain and run and you are out of the virtual environment. '''

''' Noe note after the environment created by using pipenv in the file pip.py, the import requets has an alert
    showing the pylance does not found the module requets. 
    Also if I run the pip.py file using code runner then I get same error that requests module not found. It is 
    because when I run the code from terminal the python interpretor knows where the requests module is located
    in vertual enviroment but still the vs-code does not know where the requests module located. So now we need
    to set the vertual environment path in vs code. This sectione will be discussed in env_in_vscode.py file. '''
