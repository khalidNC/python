''' In Python, there isn't explicit support for private members like in some other programming languages.
However, there is a convention that can be used to indicate that a member should be treated as private:
by prefixing its name with a single underscore (e.g., _tags). This is a signal to other programmers that
the member should not be accessed directly from outside the class. Here's how you can apply this convention
to your code: '''

class TagCloud:
    def __init__(self):
        self._tags = {}  # Using a single underscore to indicate a "private" member

    def add(self, tag):
        self._tags[tag.lower()] = self._tags.get(tag.lower(), 0) + 1
 
    def __getitem__(self, tag):
        return self._tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self._tags[tag.lower()] = count

    def __len__(self):
        return len(self._tags)
    
    def __iter__(self):
        return iter(self._tags)

cloud = TagCloud()
cloud["Python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("python")

print(cloud._tags)  # Accessing the "private" member directly (not recommended)


''' In this modified code, the member self._tags is considered "private" by convention.
However, please note that this is still not a strict form of access control;
Python does not prevent you from accessing _tags from outside the class.
It's more of a signal to other programmers that this member should not be accessed directly
and is subject to change. '''


''' If you need stronger encapsulation and access control, you can use double underscores (e.g., __tags)
to perform name mangling. This makes it more difficult to access the member from outside the class,
but it's still not true private access. Here's an example with name mangling: '''

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
 
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()
cloud["Python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
cloud.add("python")


# Accessing the "mangled" name (not recommended)
# print(cloud._TagCloud__tags)
# print(cloud.__tags)
# output: AttributeError: 'TagCloud' object has no attribute '__tags'

''' More detail on how we can access the private class:
In line 77 if we change to this;
print(cloud.__tags) 
this will return AttributeError since the class arrtibute is print and we can not access.
Now magic method __dict__ holds all the attributes of the class
os if we print this method for the class instance then we should get the attribute name and the dictionary
let's try to print. '''

print(cloud.__dict__)
# output: {'_TagCloud__tags': {'python': 14}}

''' Now if we print this attribute name for the class instance the it will return the dictionary. '''
print(cloud._TagCloud__tags)
