from timeit import timeit


''' So far we know how to raise exception. '''

my_list = [1, 2, 3]
index = 2
try:
    if index >= len(my_list): 
        raise IndexError("Index out of the range")
    
except IndexError as error:
    print('Alert:', error)

else:
    print("No exception was thrown")


''' Let's have another example: We define a custom function to calculate age: '''

age = -9
def calculate_age(age):
    if (age <= 0) or (isinstance(age, float)):
        # Check multiple conditions; if age zero or less than zero or age is a floating number
        # to compaire the age with float we need to use a built-in function isinstance(). 
        # this function takes 2 arguments. isinstance(object, classifo).
        # object = the I want to check. classinfo = The class, type, or tuple of classes/types I want to compare.
        raise ValueError("Age can not be zero, negative or a floating-point number.")
    return 100 / age

try:    
  result = calculate_age(age)
  print("Results: ", result)

except ValueError as error:
    print("Alert: ", error)

else:
    print("No exception raised.")
 

''' Raising exceptions in Python comes with some performance overhead, so it's important 
to use them judiciously. While exceptions are a powerful mechanism for error handling and 
control flow, they can be relatively slower compared to regular program execution due to 
the additional steps involved in exception propagation. So let's try to draw an example of
messuring the performance the codes with exceptions abd compaire. '''

# First, start with import timeit class from timeit module at top of the page.
# Then copy the above codes of exception and run the codes withh timeit() method and record the execution time.
# Then modify the above codes: instead raise exceptions, return none. None is an object that represent absence of value.
# Then we remove Try and Except block. Instead these we just give 1 condition if function return None then pass.
# Then run the code with timeit() method to record the execution time.
# Then compaire both codes and check which performace is better.

code1 = """
age = 9
def calculate_age(age):
    if (age <= 0) or (isinstance(age, float)):
        raise ValueError("Age can not be zero, negative or a floating-point number.")
    return 100 / age

try:    
  result = calculate_age(age)
  print("Results: ", result)

except ValueError as error:
    pass                          # Instead printing the error message just pass
    # print("Alert: ", error)       

else:
    print("No exception raised.")

"""

first_code_time_record = timeit(code1, number=1)



code2 = """
age = 9
def calculate_age(age):
    if (age <= 0) or (isinstance(age, float)):
        return None
    return 100 / age

result = calculate_age(age)
if result == None:
    pass
print("Results: ", result)

"""

second_code_time_record =  timeit(code1, number=1)

difference = first_code_time_record / second_code_time_record
print("Second code is", difference, "times faster")
# Output: Second code is 5.593970334285994 times faster
