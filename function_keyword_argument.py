''' In some cases, it is not clearly readable that the what exactly the argument is about what.
In these cases we can use keyword argument. '''

def increment(number, by):
    return number + by


# result = increment(20, 2)
result = increment(20, by=2)
print(result)

''' Here the arument 2 is may not clear to the readers, in that case we can use keyword. 
and gets the same result. '''
