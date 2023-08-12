''' Types of Functions:
So far we learnt defining a function then set parameter then call the function with
passing the arguments for the parameters. Here is the simplefy version of a
function: '''

def greet(name):
    print(f"Hey {name}")


greet("Khalid")

''' There are two types of functions:
1- Function  that performs a task
2- Function that calculate and returns value
The above example is a function that performs a task. Which is printing somethings in 
the coumputer terminal. 
In contrast, the built-in funtion round() is an example of a function that retiurn value. '''

print(round(4.5)) # that calculate and retun value 4 a round number


''' Now we are going to re-write the task performing function in value return form. We just replaced
the print with return with formated string. So we used the return statement to return the value 
from the function. 
Now call the function. Since the this is retuning the value so we can store the value in a variable,
like message.
Now there might be a question which way is better to write a function. Performing task function;
we are strict to print in terminal. But if we need to write the value in a file or we need to send 
the value as an email message then can not reuse this funtion.
On the other hand, the secound format, we store the value in a variable then we can use it in a various
ways like printing on terminal, create a file, sending emial etc. '''

def get_greeting(name):
    return f"Hey {name}"


message = get_greeting("Khalid")
print(message)
# file = open("message_content.txt", "Wrinting message")
# file.write(message)

'''open() is a built-in function to write message in a file, so we are creating a file like,
message_content.txt 
then we can store in file object. then use write() method to write the message. '''

''' Another takeout: In python all Funtions by defult return a None value. None is an object 
that represense the absence of a value. We can check the none value of a function if we 
print the function. '''

def greet(name):
    print(f"Hey {name}")


print(greet("Khalid"))

''' So all function return None unless we specificly return value. So if you return value instead print
on the above code then None will be no longer. '''

def greet(name):
    # print(f"Hey {name}")
    return f"Hye {name}"


print(greet("Khalid"))
