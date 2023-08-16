''' Default argument of function:
So far we know keyword argument of a function. '''

def increment(number, by):
    return number + by

result = increment(4, by=2)
print(result)

''' Here by=2 is the keyword argumrnt. Now we can make the parameter optional, we will not pass by=2 everytime
to the function rather we can increment the parameter value by 1.
So remove the keyword argument and give the parameter by a default value 2; by=2 
Now if we do not supply the 2nd argument then the parameter's default value will be used. 
and if we supply the 2nd argument then that value will be used. '''

def increment(number, by=2):
    return number + by

result = increment(4)
print(result)

def increment(number, by=2):
    return number + by

result = increment(4, 3)
print(result)

'''So this is the way to make parameter optional. Note that the parameter's default value
must be come after the required parameters. '''
