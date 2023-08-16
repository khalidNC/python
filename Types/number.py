# Types of numbers in Python: integer number, float number, complex number

x = 2
x = 4.9
x = 4 + 2j

# Addition, subtraction, multiplication, division

print(2 + 4)
print(4 - 1)
print(5 * 4)
print(20 / 3)

''' There are two types of division. on above the result of the division gets a float number.
If we want to get integer by ingnoring the float part then use double slash '''
print(20 // 3)   # floor division, this will return 6

print(20 % 3) # (%) is the modulus, a arithmetic operator is the remainder of a division
print(9 ** 2) # (**) is the exponentiation, a arithmetic operator of some number. Like 9 to the power 3

a = 10
b = a + 3
a += 3  # assignment oparator

print(a)

# Working with numbers
# Few built-in function/method

round_a_number = round(3.6)
print(round_a_number)

abs_number = abs(-3.6)  # absolute value of a number
print(abs_number)

''' Math module. This is a python built-in module when we work with complex mathemetical calculation the we 
import the module on the top of the page '''

import math

''' The math in this program is an object so we can use dot(.) notation to get the methods/built-in functions
from the math module of the object '''

print(math.floor(20 // 6))
print(math.ceil(2.5))

''' To get all match methods https://docs.python.org/3/library/math.html '''

# input function gets input from the user

x = input("x: ")   #x will show to user end to input the value of x, so let's call a variable for the input
y = int(x) + 3    
''' if run this program and input any value of x this will return type error. becasue x is a string.
so we need to convert the string to a number '''

# Now print the y value
print(y)

# Now print x input value and the y value
print(f"x: {x}, y: {y}")
