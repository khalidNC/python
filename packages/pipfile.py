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
invironment and can reporduce exact execution invironment. And this minimizes or eleminates the situation like the 
application that runs in your machine but does not run in other machine due have different virsion on one of this
dependencies. 

Now let's check how this works:

'''
