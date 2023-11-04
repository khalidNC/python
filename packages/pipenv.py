''' So far we know to use pip and know how to create virtual environment. 
And all the terminal command we need memorise there are lot's of things we momorise 
to make our life easy pipenv comes into the picture. This pipenv is a tool that 
combines both needs together. So we do not have to use pip and vertual environment
separately. It is a dependescy manager in python pacakages. 

So let's use pipenv. First we need to install pipenv. So write and run this command in 
terminal; 
1. pip3 install pipenv 
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
4. Now, the way to find the actual path the terminal command: python3 -m site --user-base
    a. This will return the user PATH it is like: /users/user/bin/python3.10   
4. After we complete those, install packages throgh pipenv commad like, pipenv install request
    a. This will install request for the project specially not for global.
    b. So this pipenv create virtual environment and the package same time for the project. '''
