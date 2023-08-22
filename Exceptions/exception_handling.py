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



''' Now if want to print the same error message for both except blocks then we can write both except
in 1 line code within the parenthesis. '''

try:
    dividend = int(input("Enter the divident: "))
    divisor = int(input("Enter the divisor: "))
    remainder = dividend / divisor

except (ZeroDivisionError, ValueError):
    print("Division by zero is not allowed and need valid integer value")

else:
    print("Result:", remainder)
    