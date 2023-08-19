''' Swapping variables in Python can be done using a temporary variable or through unpacking.
Here are two common methods to achieve variable swapping: '''


# 1. Using a Temporary Variable:
a = 5
b = 10

# Swapping using a temporary variable
temp = a
a = b
b = temp

print(a)  # Output: 10
print(b)  # Output: 5


# 2. Using Tuple Unpacking
a = 5
b = 10

# Swapping using tuple unpacking
a, b = b, a

print(a)  # Output: 10
print(b)  # Output: 5

'''In the second method, the values of a and b are packed into a tuple (b, a) and then unpacked back
into the variables a and b. This allows for a concise and elegant way to swap the values of two variables
without using a temporary variable. '''
