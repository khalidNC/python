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
for key, value in my_dict.items:
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


class TagCloud:
    
    def __init__(self):
        self.tags = {}
    ''' In the constructor method (__init__), an instance variable self.tags is initialized as an empty dictionary {}. 
    This dictionary will be used to store tags and their counts.'''

    def add(self, tag):
        # self.tags[tag] = self.tags.get(tag, 0) + 1
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
    ''' This method, named add, takes a tag as a parameter. Inside the method, it uses the get method of the self.tags
    dictionary to retrieve the current count of the tag. If the tag is not found in the dictionary, it defaults to 0. 
    It then increments the count by 1 and updates the dictionary with the new count. '''

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
    ''' This magic method is called when you access a tag using square brackets, like cloud["Python"]
    It returns the count of the tag from the self.tags dictionary. If the tag doesn't exist, it returns 0. '''
    
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count
    ''' This magic method is called when you assign a count to a tag using square brackets, like cloud["Python"] = 10.
    It sets the count of the tag in the self.tags dictionary to the provided value. '''
    
    def __len__(self):
        return len(self.tags)
    ''' This magic method is called when you use the len() function on an instance of the TagCould class.
    It returns the number of unique tags in the self.tags dictionary'''
    
    def __iter__(self):
        return iter(self.tags)
    ''' This magic method allows the TagCould class to be iterable.
    It returns an iterator for the keys (tags) in the self.tags dictionary.'''
    

cloud = TagCloud()
# An instance of the TagCloud class is created and assigned to the variable cloud.
cloud["Python"] = 10
# We set the count of the tag "Python" to 10 using square brackets.
len(cloud)
# We check the length of the cloud object using len(cloud), which returns the number of unique tags.
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
''' Three calls to the add method are made, each with the string "Python". This increments the count for the tag "Python"
in the self.tags dictionary.'''

cloud.add("python")
''' Now if we call add method with lowercase string"python" then the output comes {'Python': 3, 'python': 1}.
But we should catch all the text python either it is lower or upper case. to fix this, we can add python builtin method
lower() in line 157, 158.
so whatever tag we receiver here: def add(self, tag): we convert it to lower() in line 158. self.tags[tag.lower()]
as well as convert it to lower() wehn we get the tag: self.tags.get(tag.lower(), 0) + 1 line-159. '''
  
print(cloud.tags)
# This line prints the tags dictionary, which now contains the counts of the "Python" tag. Output: {'Python': 3}


''' More detail explanation of self.tags[tag] Line-158:

self.tags[tag] is used to access and manipulate a value associated with a specific key (tag) in the self.tags dictionary.

Let's break down what this expression means step by step:

self: self is a reference to the instance of the class. It allows you to access the instance's attributes and methods.
In object-oriented programming in Python, you use self to differentiate between instance variables and local variables
within a class.

self.tags: This refers to an attribute named tags that belongs to the instance. In the __init__ method, self.tags is 
initialized as an empty dictionary. So, self.tags is a dictionary used to store tags and their counts.

self.tags[tag]: This accesses a specific value in the self.tags dictionary, where tag is the key used to look up 
the value. It retrieves the current count associated with the provided tag.

self.tags.get(tag, 0): Here, the get method of the dictionary is used. It attempts to retrieve the value associated
with the tag key. If the tag is not found in the dictionary, it returns 0 as the default value.

self.tags[tag] = self.tags.get(tag, 0) + 1: This line increments the count associated with the tag key in the self.tags
dictionary. It first retrieves the current count using self.tags.get(tag, 0), adds 1 to it, and then assigns the
new count back to the tag key in the dictionary.

In essence, self.tags[tag] is a way to access the count associated with a specific tag in the self.tags dictionary.
It's a common pattern used to update values associated with keys in dictionaries. '''
