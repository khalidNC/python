''' Previously we run the pip.py file in the terminal and see the virtual environment works and package 
requests is found also the codes run successfully. But we did not run this in vs code runner. Let's see
what happened when we run this in code runner. 

We get the same error that the requests module not found. ImportError: No module named requests

It is because, when I run the code from terminal the python interpretor knows where the 
requests module is located in vertual enviroment but still the vs-code does not know where the requests 
package is located. So now we need to set the vertual environment path in vs code. 

1. Let's find the virtual environment directory: 
   Run the command: pipenv --venv
   It returns the path of virtual environment directory of you local machine.
   Which is; /Users/user/.local/share/virtualenvs/Python_Course-DQXbx9fU
   
2. Now to open this just command: open the url and run in terminal. It open the directory. Here in the
   virtual environment folder, inside the bin folder you see Python3. Now we need to get the path of this
   Python3 interpretor and give to the vs-code runner extension. 

3. Back to the vscode on the top click on the code menu 
   Then select preference 
   Then select settings
   This will open the vscode setting page
   Also you can open settings page using shortcut key: command+,

4. Now under User tab go to Text Editor section then scroll down to Code Action on Save
   here you see the option to "Edit in setting json". Click on this and it opens the 
   json setting page.

5. Here you should see the 'code-runner.executorMap' if you do not see then add key 'code-runner.executorMap'
   and hit enter it will automatically generate the settings.

   Here we can see the python key:value element is like; "python": "python -u"
   We need to set this to like: the/path/of/the/virtual/env/diretory then append this /bin/python3 
   so the setting will be, "python": "/Users/user/.local/share/virtualenvs/Python_Course-DQXbx9fU/bin/python3" 

6. Then save the changes and run the program in code runner.
   And this time it works and I see this in output:
   [Running] /Users/user/.local/share/virtualenvs/Python_Course-DQXbx9fU/bin/python3 
   "/Users/user/Desktop/Python Course/packages/pip.py"
   <Response [200]> 
   
7. Now another issue: in the pip.py file I see a alert that the python interpretor can not find the requests
   module. To fix this issue we need to set the python interpretor in virtual environment dir in vs code.
   To do so click on the python version number at buttom of the vscode windo. It will open the dropdown on the 
   top having the python interpretor in vertual environment just select this one. 

   If you do not see the python interpretor on the top dropdown then go to the settings.json file once again 
   and add a setting, "python.pythonPath": "/Users/user/.local/share/virtualenvs/Python_Course-DQXbx9fU/bin/python3",
   After we add this we should see the interpretor at the top dropdown.

   Note: you may need to restart the vscode after have the chnages. '''
