import sys


print(sys.argv)
# OutPut: ['library/library_commandline_argument.py']


# Check sys.argv has atleast 1 item
# Then print a usage message and after that we expect a password
# Else when the user give additional argument as password we will read it like this
if len(sys.argv) == 1:
  print("USAGE: python library_commandline_argument.py <password>")

else:
  # sys.argv[1], means the 2nd item in the array is the password
  password = sys.argv[1]
  # Let's print the password in terminal
  print("Password:", password)


''' While we work with python language that expects command line arguments. Just like python program
itself when we write command(python3 file_name.py) this is command line argument.
Now we will extend this next level and supply additional argument in the command, this 
argument can be the name of a user, email, password or wahtever like this; python3 file_name.py -a -b -c

Let's start with import sys module. This module has an attribute called argv (argument variable)
So let's print sys.argv and execute the command line: python library/library_commandline_argument.py
and see what we get;

OutPut: ['library/library_commandline_argument.py']

Now execute the command line: python library/library_commandline_argument.py -a -b -c and print(sys.argv)
now the OutPut: ['library/library_commandline_argument.py', '-a', '-b', '-c']

We see a list of 4 items, The first item is always our python file. Even we do not supply any additional
argument this print(sys.argv) returns list of 1 item, which is out python file. 

Rest of others are the items of the arguments and we can do an iterresting thing out these;
We can get the len(sys.argv) of this array and if it is equal to 1 that means user does not supply any
argument because this array always has atlease 1 item in it which is our python file.
Then print a usage message and after that we expect a password
Else when the user give additional argument as password we will read it like this in codes line-14.

Now first execute the commad-line: python library/library_commandline_argument.py
And the OutPut: USAGE: python library_commandline_argument.py <password>
so it expect a password.

Now execute command line: USAGE: python library_commandline_argument.py 1234
And the OutPut:
Password: 1234 '''

''' argparse library and few examples of command line arguments: 
Command line arguments allow you to pass input parameters to your Python scripts when 
they are executed from the command line. Python provides the argparse library as part of 
the standard library to easily handle command line arguments. The argparse library simplifies 
the process of defining and parsing command line arguments, making it a powerful tool for 
creating flexible and user-friendly command line interfaces for your Python programs. 

Here's an overview of how to use the argparse library to work with command line arguments in Python:

1. Import the argparse Module: import argparse

First, you need to import the argparse module in your Python script. 

2. Create an Argument Parser:
You need to create an ArgumentParser object, which will handle the parsing of command line arguments.

3. Define Command Line Arguments:
You can define the arguments that your script accepts using the add_argument() method of the 
ArgumentParser object.

4. Parse Command Line Arguments:
Use the parse_args() method to parse the command line arguments and store them in a namespace.

5. Access Parsed Arguments:
You can access the values of parsed arguments by using the dot notation on the args namespace. '''

import argparse

parser = argparse.ArgumentParser(description="Description of your program.")
# The description argument is optional and is used to provide a brief description of your program.

parser.add_argument("arg_name", help="Help message for this argument.")
# "arg_name" is the name of the argument (e.g., "--input-file").
# help is a brief description of what the argument does.

args = parser.parse_args()

print(args.arg_name)


''' Now a real example of reading a file from the computer with command line argument:
To do so we need to write a script as below; 

1. Import argparse module:
   we import the argparse module, which provides the functionality for parsing command line arguments.
   
2. Define the main Function: 
   We define a function named main that will contain the main logic of our script.
   
3. Create an Argument Parser:
   Here, we create an ArgumentParser object named parser. We provide a description for our program 
   using the description parameter. This description will be displayed when users request help using 
   the --help argument. 
   
4. Define Command Line Arguments:
   We define a command line argument named "filename". The help parameter provides a brief description 
   of what this argument does. In this case, it specifies that it's the path to the file to print.
   
5. Parse Command Line Arguments:
   we parse the command line arguments provided to our script and store the results in the args variable. 
   This allows us to access the values of the parsed arguments.
   
6. Read and Print the File Content:
   Here, we open the file specified by args.filename in read mode ('r'). We then read the content of the 
   file and print it to the console. We use a try block to handle exceptions:
      a. If the file is not found (raises FileNotFoundError), we catch the exception and print a specific 
         error message.
      b. If any other exception occurs, we catch it and print a general error message along with the 
         exception details.

7. Main function and Run Script:
    Main function: 
    This conditional(if __name__ == "__main__") block checks if the script is being run as the main program. 
    If so, it calls the main() function. This structure is commonly used to make the script reusable as a 
    module and executable as a standalone script.

    Run script:
    To run the script the command line argument will be:
    python library/library_commandline_argument.py movies.json (There is a file movies.json in my machine)

    OutPut:
    File Content:
    [{"id": 1, "name": "Terminator", "Year": "1989"}, {"id": 2, "name": "Predator", "Year": "1987"}] '''

def main():
    parser = argparse.ArgumentParser(description="Print the content of a file.")
    parser.add_argument("filename", help="Path to the file to print.")

    args = parser.parse_args()
    
    try:
        with open(args.filename, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"File not found: {args.filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
