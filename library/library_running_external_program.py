import subprocess


# subprocess.run(["ls", "-l"])
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

# results = subprocess.run(["ls", "-l"])
# print(type(results))
# OutPut: <class 'subprocess.CompletedProcess'>, a instance of the class

# completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
# completed = subprocess.run(["python", "other.py"], capture_output=True, text=True)
completed = subprocess.run(["false"], capture_output=True, text=True, check=True)
print("Argument", completed.args)
print("Returncode", completed.returncode)
print("Standard error", completed.stderr)
print("Standard output", completed.stdout)

if completed.returncode != 0:
  print(completed.stderr)

''' Here we will mainly look at;
How to call external program from python script. 
This is perticularly usefull sepecially part of automation script.
For example: Let's say, you want your python program to run the las command and capture the output.
In Mac this commad lists the files and directories in current directory, like this: 
Classes         Data structure  Functions       README.md       data.csv        extract         
khalid.png      movies.json     Control flow    Exceptions      Modules         Types           
db.sqlite3      files.zip       library         template.html 

So here we will discuse:
1. How to run any of the oparating system command 
2. As well as external programs

For example, your python script exucutes anpther python script.

For that we need to run in terminal let's say, python other.py 

To achive this;
1. First we need to import the subprocess module. With this module we can get a child porcess, a porcess
   is basically an inctance of a running program. So with this module we can run other program. 
   
2. Now in this module we have a bunch of functions or methods like, .call, .check_call, .check_output, 
   and so on. All this methods are helper methods to create an instence of Popen class to process open.
   Now these .call, .check_call, .check_output method are old and they are considered kind of legacy.
   So there is latest method call .run that is the prefered approach to create an instance of the Popen
   class.
   
3. Now let's see how we can use the run method to an external program.
   The first argument of this method, is an array of string. Here is an example; Let's say we want to
   run the ls command so keep "ls" in the list - run(["ls]).
   
   Now if you want to supply additional argument to this command, we can add the as an item in this 
   array like this run(["ls", "-l"]) which returns us a detail view of the files and directories.
   in the current directory. 
   
   If we command ls -l in terminal we get output:
   
   total 168
   drwxr-xr-x  23 Khalid  staff    736 Sep 25 07:24 Classes
   drwxr-xr-x   9 Khalid  staff    288 Aug 22 14:21 Control flow
   drwxr-xr-x  25 Khalid  staff    800 Aug 22 14:21 Data structure
   drwxr-xr-x   8 Khalid  staff    256 Aug 24 17:04 Exceptions
   drwxr-xr-x  10 Khalid  staff    320 Aug 22 14:04 Functions
   drwxr-xr-x  15 Khalid  staff    480 Oct 10 15:19 Modules
   -rw-r--r--   1 Khalid  staff   1557 Aug  6 17:17 README.md
   drwxr-xr-x   5 Khalid  staff    160 Aug 16 15:34 Types
   -rw-r--r--   1 Khalid  staff     49 Oct 13 21:27 data.csv
   -rw-r--r--   1 Khalid  staff  12288 Oct 15 20:09 db.sqlite3
   drwxr-xr-x   3 Khalid  staff     96 Oct 12 21:10 extract
   -rw-r--r--   1 Khalid  staff   6336 Oct 12 20:16 files.zip
   -rw-r--r--@  1 Khalid  staff  45858 Oct 19 14:04 khalid.png
   drwxr-xr-x  19 Khalid  staff    608 Oct 23 18:17 library
   -rw-r--r--   1 Khalid  staff     96 Oct 14 22:31 movies.json
   -rw-r--r--   1 Khalid  staff   3016 Oct 20 23:42 template.html
   
   So we get file, creation date, time, size, Owner etc.

4. Now we run the program with the python commad: python library/library_running_external_program.py
   And we see the command excuted and I get exactly the same results as above. 

5. Now, let's look at the return value of this method. So let's define a variable result and store 
   the value of the method. Then print the type of the result. What we get is the instance of this 
   class: <class 'subprocess.CompletedProcess'>

6. Then rename the result variable to completed. And now look at the attributes of this object
   we have completed.args, .returncode, .stnerr (short from of standard error), .stdout short from
   of standard output. Let's inspect each of this attributes;
      1. Print .args and for clarity add a level like print("Argument:", completed.rgs)
      2. Print .returncode and for clarity add a level like print("ReturnCode:", completed.returncode)
      3. Print .stnerr and for clarity add a level like print("Standard error:", completed.stnerr)
      4. Print .stdout and for clarity add a level like print("Standard output:", completed.stdout)
   Now run the program and see what we get; 
                                            Argument ['ls', '-l']
                                            Returncode 0
                                            Standard error None
                                            Standard output None
   
   So Argumants is the command we give to execute.
   Returncode 0 zero which means sucess, any non zero vale indicates error.
   In this case, since we do not have any error the standard error is None, Otherwise here would
   have an error message.
   And the standard output is also None because we are not capturing the output here. Output is
   automatically printed in the terminal. Sometimes we read the output from another program and do
   something with it. Like, save this to another file. 

   To do this, we need to pass 2nd argument as keyword=argument to the run() method. e.g 
   capture_output= if this set this to True and run the program then output will not be printed 
   on the terminal rather it will save on .stdout attribute.

   Let's take a look, I am going to comment out the print(completed.stdout) and run the program.
   And I do not get output in the terminal. 
   OutPut:
          Argument ['ls', '-l']
          Returncode 0
          Standard error b''
   
   So the output is in completed.stdout attribute. Now print the attribute and let's see what we
   get.
   OutPut:
   Argument ['ls', '-l']
   Returncode 0
   Standard error b''
   Standard output b'total 168\ndrwxr-xr-x  23 Khalid  staff    736 Sep 25 07:24 Classes\ndrwxr-xr-x   
   9 Khalid  staff    288 Aug 22 14:21 Control flow\ndrwxr-xr-x  25 Khalid  staff    800 
   Aug 22 14:21 Data structure\ndrwxr-xr-x   8 Khalid  staff    256 Aug 24 17:04 Exceptions\ndrwxr-xr-x  
   10 Khalid  staff    320 Aug 22 14:04 Functions\ndrwxr-xr-x  15 Khalid  staff    
   480 Oct 10 15:19 Modules\n-rw-r--r--   1 Khalid  staff   1557 Aug  6 17:17 README.md\ndrwxr-xr-x   
   5 Khalid  staff    160 Aug 16 15:34 Types\n-rw-r--r--   1 Khalid  staff     
   49 Oct 13 21:27 data.csv\n-rw-r--r--   1 Khalid  staff  12288 Oct 15 20:09 db.sqlite3\ndrwxr-xr-x   
   3 Khalid  staff     96 Oct 12 21:10 extract\n-rw-r--r--   1 Khalid  staff   
   6336 Oct 12 20:16 files.zip\n-rw-r--r--@  1 Khalid  staff  45858 Oct 19 14:04 khalid.png\ndrwxr-xr-x  
   19 Khalid  staff    608 Oct 23 18:17 library\n-rw-r--r--   1 Khalid  staff     
   96 Oct 14 22:31 movies.json\n-rw-r--r--   1 Khalid  staff   3016 Oct 20 23:42 template.html\n'

   Note: In the output we get a string prefix with b this represents binary object. To fix this we need 
   to pass another keyword=argument text=True. Then run the program once again and this time we get 
   regular string as output.
   OutPut:
   Argument ['ls', '-l']
   Returncode 0
   Standard error 
   Standard output total 168
   drwxr-xr-x  23 Khalid  staff    736 Sep 25 07:24 Classes
   drwxr-xr-x   9 Khalid  staff    288 Aug 22 14:21 Control flow
   drwxr-xr-x  25 Khalid  staff    800 Aug 22 14:21 Data structure
   drwxr-xr-x   8 Khalid  staff    256 Aug 24 17:04 Exceptions
   drwxr-xr-x  10 Khalid  staff    320 Aug 22 14:04 Functions
   drwxr-xr-x  15 Khalid  staff    480 Oct 10 15:19 Modules
   -rw-r--r--   1 Khalid  staff   1557 Aug  6 17:17 README.md
   drwxr-xr-x   5 Khalid  staff    160 Aug 16 15:34 Types
   -rw-r--r--   1 Khalid  staff     49 Oct 13 21:27 data.csv
   -rw-r--r--   1 Khalid  staff  12288 Oct 15 20:09 db.sqlite3
   drwxr-xr-x   3 Khalid  staff     96 Oct 12 21:10 extract
   -rw-r--r--   1 Khalid  staff   6336 Oct 12 20:16 files.zip
   -rw-r--r--@  1 Khalid  staff  45858 Oct 19 14:04 khalid.png
   drwxr-xr-x  19 Khalid  staff    608 Oct 23 18:17 library
   -rw-r--r--   1 Khalid  staff     96 Oct 14 22:31 movies.json
   -rw-r--r--   1 Khalid  staff   3016 Oct 20 23:42 template.html

Now we can print this in terminal or save in to a file. 

Let's run another python script. I have created a python file in current directory, let's say other.py
Let's assume this other.py file is a complicated script and we want to call this as part of running
our main script. So for the time being we just write a single line code in the file as 
print("This is a complicated script") so that when we run the program it shows in the terminal.

So go back to the main file and we can simply raun this script as child process
so instead of run(["ls", "-l"]) write ["python", "other.py"]. First we execute python program then 
the file. Now save the changes and run the program once again and see the output.
OutPut:
Argument ['python', 'other.py']
Returncode 0
Standard error 
Standard output This is a complicated script.

As we can see the other script is executed and it captured the ouput.

Note: We executed the other script as child process. So it is in completely a separate memory space.

This is the basic of running child process. '''

''' Another thing, if there is an non zero codereturn that indicates an error. So let's take a look
on a real example, if we pass "false" as argument in run(["false"]) method then the output we get:
Argument ['false']
Returncode 1
Standard error 
Standard output

See, we get returncode 1 because the false program returns the returncode 1. Indicates an error.
So our job is to check for error;
1. so one way is to check with if condition. Like if returncode is not equal to zero then print 
   .stderr attribute. 

2. The another approach is to pass another keyword=argument(check=True) to the run() method. If 
   do this then if there is any error then the run() method automatically raise an error. 
   Let's take a look. We run the program and the output: 
   subprocess.CalledProcessError: Command '['false']' returned non-zero exit status 1.

   See got a exception error type "CalledProcessError" and this class is define in subprocess 
   module. 

3. So finally, we can complete this code with the try block.   

'''