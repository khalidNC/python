''' When we install a packagess useing pipenv 2 files are automatically created, Pipfile and Pipfile.lock these
2 files are use to keep track of the dependencies of our project 

The primary purpose of a Pipfile is to specify the dependencies for your Python project. It lists all the packages 
and their versions required for your project to run correctly. These dependencies are typically stored under four 
sections: [Source] [dev-packages] [packages] and [Requires]

[Source]: Has an url where the packages are downloaded from.
[dev-packages]: This section contains dependencies required for development, such as testing frameworks, linters, 
or tools used during development.
[packages]: This section contains the main project dependencies required for the application to function in production.
[Requires]: That specify the python version that required for the project.

Now take a look at our Pipfile.lock:
This is a json file that list all the depedencies for our application and their exact verison.
Let check it out:

meta: Here at the top we have section called  _meta: 
 default: Below that we have default: inside of it we have all the dependencies and their exact version.
   certify: Here the depedencies of the packages are listed and the version. If we scroll down we can see the request
            package and the version that we installed in our local machine.

Now all the infomation in this file we can take the source code and put these in anpther machine like a production
invironment and can reporduce exact execution invironment. And this minimizes or eleminates the situation where your 
application runs in your machine but does not run in other machine due have different virsion on one of this
dependencies. 

Now let's check how this works:
1. Let's find the virtual environment for this project: terminal command: pipenv --nenv
   Output: /Users/user/.local/share/virtualenvs/Python_Course-DQXbx9fU
   this is the virtual environment directory link. And I am going to delete this link now to create a scenario
   where we copy our project into another machine on that machine this virtual envirment doe not exist, all we
   have the source code of our application.  

2. Delete the directory: In mac or linex the terminal command to delete directory is: rm -rf the path of dir
   terminal command: rm -rf /Users/user/.local/share/virtualenvs/Python_Course-DQXbx9fU
   and file deleted.
   Again command: pipenv --venv
   Output: No virtualenv has been created for this project/Users/user/Desktop/Python Course yet!
   since the directory is deleted. 
   Now only have the source code and Pipfile and Pipfile.lock that specify the dependency of the project.

3. Now we need to install all this dependencies. This is very easy, just we need to run pipenv install.
   When we run this command this will check the Pipfile and install all the dependencies. Let's do it.
   pipenv install
   This install the dependency on pipfile and creates the virtual environment.
   Run the pipenv --venv command once again and it returns the path of the virtual environment directory.
   Output: /Users/user/.local/share/virtualenvs/Python_Course-DQXbx9fU

   So all the dependencies installed based on the packages version mentioned in the pipfile:
        [[source]]
        url = "https://pypi.org/simple"
        verify_ssl = true
        name = "pypi"

        [packages]
        requests = "*"

        [dev-packages]

        [requires]
        python_version = "3.10.0" 
  
   Now in the pipfile we see the request package version is the latest one and on the lock the request version
   is 2.31.0. Later if we opne the porject in a different machine and run the program we might need a newer version
   of request package. In that case, the dependency install in other machine deferrent that in my machine. 
   So if we want to install exactly same as listed in lock file. Then we need to ignore the pipfile and need to 
   use the lock file while installing pipenv. Let's see the command in terminal:
       
        pipenv install --ignore-pipfile 
        
    Output: Installing dependencies from Pipfile.lock (479990)... '''
