''' Creating custom containers in Python involves defining your own classes that behave
like built-in data structures such as lists, dictionaries, or sets. To create a custom
container, you need to implement methods that enable your class to mimic the expected
behavior of the built-in container types. Here's an example of creating a simple custom
container that behaves like a list: '''

class MyList:
    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

my_list = MyList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list)      # Output: [1, 2, 3]
print(my_list[1])   # Output: 2
print(len(my_list)) # Output: 3

''' In this example, we've created a custom container MyList with some of the methods typically found in a list:

__init__(self): The constructor initializes the container's internal data structure, which is a list in this case.

append(self, item): This method allows you to add elements to the custom list.

__getitem__(self, index): This magic method is called when you use square brackets to access elements by index.

__len__(self): This magic method is called when you use the len() function on an instance of MyList.

__str__(self): This magic method is called when you use the str() function or print() on an instance of MyList.

You can expand on this basic example to create more complex custom containers. For example, you could create a custom 
dictionary-like container by implementing __getitem__, __setitem__, __delitem__, and other relevant methods. '''


''' Here's a simple example of a custom dictionary-like container: '''

class MyDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

my_dict = MyDict()
my_dict["name"] = "Alice"
my_dict["age"] = 30

print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
del my_dict["age"]
print(my_dict)          # Output: {'name': 'Alice'}


''' Now we are creating a custom container that behaves like a dictionary defining a class 
and implementing several methods, including __getitem__, __setitem__, __delitem__, and __iter__.
The __iter__ method allows your custom container to be iterable, which means you can loop through
its keys or items. Let's create a custom dictionary-like container and break down the code step by step: '''

class MyDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data.keys())

my_dict = MyDict()
my_dict["name"] = "Alice"
my_dict["age"] = 30

# Iterating through keys using a for loop
for key in my_dict:
    print(key)  # Output: name, age

# Using the items stored in the custom dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Output: name: Alice, age: 30

''' Let's break down the code step by step:

Class Definition:
We define a class called MyDict to create our custom dictionary.

Constructor (__init__):
In the constructor, we initialize the container's internal data structure. Here, we use a regular 
dictionary called self.data to store key-value pairs.

__getitem__(self, key):
This method is called when you access a key in the custom dictionary using square brackets (my_dict[key]). 
It returns the corresponding value from the internal dictionary.

__setitem__(self, key, value):
This method is called when you assign a value to a key in the custom dictionary (my_dict[key] = value).
It sets the key-value pair in the internal dictionary.

__delitem__(self, key):
This method is called when you delete a key from the custom dictionary (del my_dict[key]). It deletes
the key-value pair from the internal dictionary.

__iter__(self):
This is the __iter__ magic method. It returns an iterator object over the keys of the custom dictionary.
In this example, we use iter(self.data.keys()) to iterate through the keys of the internal dictionary.
Creating an Instance of MyDict:

We create an instance of MyDict called my_dict.
Manipulating and Iterating Through the Custom Dictionary:

We add key-value pairs to my_dict using square brackets (my_dict["name"] = "Alice").

We then demonstrate two ways to iterate through the custom dictionary:
First, we use a for loop to iterate through the keys.
Second, we use a for loop to iterate through key-value pairs.

By implementing these methods, you've created a custom dictionary-like container that you can use
and iterate through like a standard Python dictionary. '''


''' Let's have another example: lets's say we have a class TagCloud we will implement this to track 
various numbers of tags in a blog. Like, we can find the numbers of articles tagged "python" in Python
library. '''


class TagCould:
    
    def __init__(self):
        self.tag = {}

    # def add(self, tag);
  
