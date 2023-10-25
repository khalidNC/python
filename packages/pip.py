''' To use the pypi packages we use the tool called pip. For ean example we want to install
a package called requests then we will go to terminal and commad pip install requests
when we hit enter button then it wil start downloading and installing the requests package.
Then you will see the success message after this is installed.

Now if the current version of your pip is old then you will gat a warning in yellow color,
it asks you to upgrade the current viersion of pip. So We need to update pip time to time. 

The waring message is like this:
WARNING: You are using pip version 21.2.3; however, version 23.3.1 is available.
You should consider upgrading via the 
'/Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10 -m pip install --upgrade pip' 
command. 

So after we run the command it downloaded and install the the latest pip program in my mac.
also I can see the last version number as well as the newly updated version as below;

Requirement already satisfied: pip in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (21.2.3)
Collecting pip
  Downloading pip-23.3.1-py3-none-any.whl (2.1 MB)
     |████████████████████████████████| 2.1 MB 82 kB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.3
    Uninstalling pip-21.2.3:
      Successfully uninstalled pip-21.2.3
Successfully installed pip-23.3.1 

After that if i run any pip command like: pip list 
I get the list of all installed packages but this time I do not get the warning message. '''

''' 
Semantic version:
In the list we get results like this way;
Package           Version
----------------- --------
pip               23.3.1
python-dateutil   2.8.2
requests          2.25.1
selenium          4.10.0

Here in version number the first number represents the main version.
The second number represents minor version.
And the third number represents the patches or the bugs fixes.

Now if you go to th pypi.org site and search for a package let's say search for requests.
Then open a packages here in this page you see release history so click on it and it will
land you on the release history page for the packages: https://pypi.org/project/requests/#history
here you can see all the version with date of release. 

So let's say you install your package with pip command: pip install requests. After that you 
are ready to use the features of the package in your codes. 

For an example: You import requests module then use method get()
then print(the response) '''

import requests


response = requests.get("https://google.com")
print(response)
# OutPut: <Response [200]>
