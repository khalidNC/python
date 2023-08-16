''' We going to write fizzbuzz algorithm. The task is;
if the input number is divisible by 3 then it returns Fizz
if the input number is divisible by 5 then it returns Buzz
if the input number is divisible by 3 and 5 both then it retunrs FizzBuzz
rest of others input it returns the input back. '''

''' To sovle this let's difne a function fizz_buzz and set parameter as input.
Then check either the input is divisible by 3 and set a variable result is Fizz.
else the result is Buzz. then it retrun result. and call the function.'''

# def fizz_buzz(input):
#     if input % 3 == 0:
#         result = "Fizz"
#     else:
#         result = "Buzz"
#     return result


# print(fizz_buzz(5))


''' We can rewrite the codes in more better way.
Rather we declear a vareable results then return it we simple directly return.'''

# def fizz_buzz(input):
#     if input % 3 == 0:
#         return "Fizz"
#     else:
#         return "Buzz"


# print(fizz_buzz(5))


''' Another way to make the codes more improvise and cleaner. The function has the if statement and it is 
returning a value so we do not really need else statement. Because when if statement is true and
it is returning the value the python interpreter moves to the next return. So we can delete else. Let's 
remove else and correct the indentation before 2nd return then run and check we get same results or not. '''

# def fizz_buzz(input):
#     if input % 3 == 0:
#         return "Fizz"
#     return "Buzz"


# print(fizz_buzz(5))


''' Now we will give our 2nd condition that the inout is divisible by 5 return Buzz. 
Here we do not really need elif because if the first condition comes false program 
default moves to next. so for 2nd conditin we write if condition. Also in same way we 
write the 3rd condition, if input divisible by 3 and 5 both then return FizzBuzz. Finaly,
return input for everything else. '''

# def fizz_buzz(input):
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     if (input % 3 == 0) and (input % 5 == 0):     # Since the condition is long put them into parenthesis
#         return "FizzBuzz"
#     return(input)
    

# print(fizz_buzz(15))


''' Now run the program with argument 3 and it returns Fizz, which is corrent. 
then run with argument 5 and it returns Buzz, which is also correct.
then run with argument 15 which is divisible by 3 and 5 both but it returns Fizz again. This is
returning Fizz because 15 is divisible by 3 which the first condition so it ends up here and 
not moving to the 2nd or third.
So to fix this we need to move the 3rd condition to top and run and check. '''

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):     # Since the condition is long put them into parenthesis
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return(input)
    

print(fizz_buzz(46))

''' Now the program is running well meeting all the conditions. '''
