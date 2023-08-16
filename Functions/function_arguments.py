# So far we difine function.
def greetings():
    print("Hey there")
    print("Welcome to the python world")


greetings()

''' Here the print function takes input but the greetings function does not take any input.
Now we will input the first name and last name to the function.
When difining a function inbetween the parenthesis we list our Parameters;
Here we give first_name, last_name
Now when we call the function, we need to supply the values of those parameters(we call the arguments)
inbetween the parenthesis; Here we set the value "Khalid", "Hussain" 
These are the arguments of the greetings() function and
the inputs(first_name, last_name) are the Parameters when defining the function.
Now we need to print actual name insted "Hey there". So format the string for print method.
Removing "there" and passing two fields(first_name, last_name) here with curly brackets. '''

def greetings(first_name, last_name):
    print(f"Hey {first_name} {last_name}")
    print("Welcome to the python world")


greetings("Khalid", "Hussain")
