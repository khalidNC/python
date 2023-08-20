''' In Python, a dictionary is a built-in data structure that allows you to store 
and manage collections of key-value pairs. Each key in a dictionary is unique, and it is 
associated with a corresponding value. Dictionaries are also known as associative arrays 
or hash maps in other programming languages.

Here's how you can work with dictionaries in Python: '''

# Empty dictionary just curly brackets
point = {}

# Now put key and value in the dictionary, here key is x and it's value is 1
point = {"x": 1, "y": 2}

# Creating a dictionary with dict() method, This buitl-in fucntion needs keyword arguments. Syntax: x=1
point = dict(x=1, y=2, c=3)
print(point)                    # Output: {'x': 1, 'y': 2, 'c': 3}

# Index the key and get value as return.
print(point["x"])

# If you want to change the value of "x" 1 to 10 then
point["x"] = 10
print(point)                    # Output: {'x': 10, 'y': 2, 'c': 3}

# We can add a new key
point["z"] = 7
print(point)                    # Output: {'x': 10, 'y': 2, 'c': 3, 'z': 7}


# Now if we index an invalid key
# point["a"]
# print(point["a"])               # Here we get KeyError: 'a' since "a" is not in the list

# Now we can solve thie in two ways:
# 1. We can check the key is present in the dictionary or not by in statement
if "a" in point:
    print("Yes")

else:
    print("No")

# or we can check with print this will return boolean True/False
print("z" in point)

# 2. we can use get() method. It takes argument as key and returns default None for no key. If key is there
# the it returns value of that key.
point.get("a")
print(point.get("a"))

# Here it default returns None for no key, so we can pass second argument like if there is no key return zero 
print(point.get("a", 0))

# For deletinng key: value use del function
del point["x"]
print(point)                    # Output: {'y': 2, 'c': 3, 'z': 7} x=10 has been deleted

# Loop over dictionary. I we do for statement then it returns key.
for key in point:
    print(key)                  # Output: y c z

# Now we can print key and value just pass the dictionary[key] as another argument
for key in point:
    print(key, point[key])      # Output: y 2 c 3 z 7

# There is another way to iterate over dictionary. On for statement we use items() for dictionary
for key in point.items():
    print(key)                  # Output: we get ("key", value) tuple

for key, value in point.items():       # Now we are unpacking the tuple key, value. 
    print(key, value)                  # And we get same result as on line-63
