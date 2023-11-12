''' There are couple of usefull pipenv commands to manage the dependencies:

1. pipenv graph: Run this command to see all the list of installed packages: 
    Output:
            requests==2.31.0
            ├── certifi [required: >=2017.4.17, installed: 2023.7.22]
            ├── charset-normalizer [required: >=2,<4, installed: 3.3.2]
            ├── idna [required: >=2.5,<4, installed: 3.4]
            └── urllib3 [required: >=1.21.1,<3, installed: 2.0.7]

            Here we see we have requests package version 2.31.0
            and the list of all dependencies on requests package itself.

            And it also show the required version for the requests packages and the version installed.
            
2. Now if we uninstall the requests package: Terminal command: pipenv uninstall requets
   It removes the requests package and we can not see this anymore on Pipfile:
    Pipifile:
              [[source]]
              url = "https://pypi.org/simple"
              verify_ssl = true
              name = "pypi"

              [packages]

              [dev-packages]

              [requires]
              python_version = "3.10.0"

   Also it does not return when we run command: pipenv graph
        OutPut:
               certifi==2023.7.22
               charset-normalizer==3.3.2
               idna==3.4
               urllib3==2.0.7
   Though it returns the dependencies of the requests packages, because pipenv does not know it the package 
   is still use somewhere else or not.
  
   However if we put this project in other machine then these dependencies will not shows up since in Pipfile
   the requests package does not exist anymore.

3. Now install the previous version of requests package which is 2.30.0
   The terminal command: pipenv install requests==2.30.* 
   this installs the 2.30 latest version. 
   
   Now in Pipfile we can see under packages: requests = "==2.30.*"
   And on Pipfile.loc we can see the actual version "version": "==2.30.0"

3. Now time to look at the outdated packages:
   The terminal command to check outdated package:
   
   pipenv update --outdated
   
   Output:
          ✔ Success!
          Skipped Update of Package requests: 2.30.0 installed, {rdeps['required']} required (==2.30.* set in Pipfile),
          2.31.0 available.
          All packages are up to date!

   I see the success message but there is a warning message in yellow color: saying that requests package is skipped
   updating because in Pipfile referrence the required packages 2.30.* but latest version is avialable. 

4. To fix this go to Pipfile and change the requests packege vrsion to 2.31.* as latest compatable version for the 
   project. Then run the command: pipenv update --outdated one more time and this time I do not see the warning
   message.

   Output:
   Package 'requests' out-of-date: {'version': '==2.30.0', 'editable': False, 'extras': []} installed, '==2.31.0' available.

5. Update the packages: Now we have 2 choices: update all packages or update single package
   Terminal command to update all packages:
        pipenv update
    
   And command for updating a singe package:
        pipenv update requests(the name of the package)

   Now let's run pipenv update requests

   Output:
      Installing dependencies from Pipfile.lock (479990)...
      To activate this project's virtualenv, run pipenv shell.
      Alternatively, run a command inside the virtualenv with pipenv run.
      All dependencies are now up-to-date!

    and in Pipfile we see:
          [packages]
          requests = "*"
    and on Pipfile.lock we see:
          "version": "==2.31.0" '''
