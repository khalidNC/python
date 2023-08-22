''' Here are a couple of basic examples of how to handel exception error: '''

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator

except ZeroDivisionError:
    print("Division by zero is not allowed.")

except ValueError:
    print("Please enter valid integer values.")

else:
    print("Result:", result)

''' In this example:
The try block attempts to get input from the user, perform a division operation, and store the result.

* If a ZeroDivisionError occurs (division by zero), the program jumps to the corresponding except block 
and prints an error message.

* If a ValueError occurs (non-integer input), the program jumps to the second except block and prints an error message.

* If neither of these exceptions occurs, the else block is executed, and the result is printed. '''



''' Now if want to print the same error message for both except blocks then we can write both exceptions
in 1 line code within the parenthesis and comma separated. '''

try:
    dividend = int(input("Enter the divident: "))
    divisor = int(input("Enter the divisor: "))
    remainder = dividend / divisor

except (ZeroDivisionError, ValueError):
    print("Division by zero is not allowed and need valid integer value")

else:
    print("Result:", remainder)



''' Another trick to print a detail error message if there is exceptions. We can define a variable
that will incude the detail of the execption mostly the error message and additional argument.
Syntax: execptionType as ex/exception/error etc jus define variable: 
then print(ex/exception/error etc the variable) this
also print(type(ex/exception/error etc the variable)) '''

''' Let's check with the below example: '''

try:
    age = int(input("Age: "))

except ValueError as hhh:
    print("Enter a valid age")
    print(hhh)
    print(type(hhh))

else:
    print("No exception was thrown")
print("Prgram continues")

''' Now if we run the program and input a non numeric value the error message shows like;
Enter a valid age                              => this the custom error message
invalid literal for int() with base 10: 'a'    => Actual error message
<class 'ValueError'>                           => Actual error message '''  
