from sys import getsizeof


''' A generator expression in Python is a compact and memory-efficient way to create an iterator.
It's similar in concept to a list comprehension or a dictionary comprehension, but instead of 
creating a list or dictionary, it generates values one at a time as you iterate over them.
This is particularly useful when dealing with large datasets or when you want to avoid storing
all values in memory at once.

The syntax for a generator expression is quite similar to a list comprehension:
(expression for element in iterable)

So The key difference with the list comprehension is that generator expressions use parentheses() 
instead of square brackets [].

Here's an example of a generator expression: '''

# Creating a generator expression
numbers = [1, 2, 3, 4, 5]
squared_generator = (num ** 2 for num in numbers)
print(squared_generator)                      # Output: <generator object <genexpr> at 0x10d065d20>

# Using the generator to retrieve values
for squared_num in squared_generator:
    print(squared_num)                        # Output: 1 4 9 16 25


''' Notice that the generator expression doesn't create a list containing all squared numbers immediately.
Instead, it generates each squared number as you iterate over it, saving memory. Generator expressions
are especially useful when you want to iterate over a large dataset or when you're working with streams
of data that don't need to be stored entirely in memory. They can be used in places where you would use
a list comprehension, like in loops, function calls, and more. 

Keep in mind that once you've iterated through a generator expression, you can't go back and iterate over
it again, as it's an iterator that produces values on-the-fly. If you need to iterate over the values
multiple times, you might want to consider using a list comprehension to create a list or converting the
generator to a list using the list() function. '''

''' Let's have another example: 
We are creating a list with list comprehension '''

values = [x *2 for x in range(11)]
for x in values:
    print(x)

''' For example if the range is thousands or millions then creating the list is not memory effecient. 
In this situstion we use generator. Generator is alose iterable, each iteration it genarates value
but not store it in memory. 

Now we just replace the square brackets with parenthesis() and save the changes and run and get 
same results. '''

values = (x *2 for x in range(11))
for x in values:
    print(x)

''' However the values now is no longer a list it is noe generator. Let's us check if we just 
print values we get the output generator object. Which is a iterable so each iteration it retruns 
value. But what is interesting the size of genarator object. 

Let's check how to get the size of generator object. 
So on the top of the page we import class getsizeof from sys module
Now in the generator let's change the range to 1000
and then pass the generator in getsizeof() method 
Then print the generator. In output we get the generator size in bits. 
And let's put a lebel "Gen" '''

generator_values = (x * 2 for x in range(100000))
getsizeof(generator_values)
print("Gen:", getsizeof(generator_values))            # Output: 104 bits

# Now change the range 100,000 and see still the size is 104 bits

''' Now to make a contrast we will get the size of the same range 100,000 and see the sixe in memory bits.
Let's copy the codes and make it list with suqare brackets and put a lebel in print method "list" 
then save and run the codes and compare the size in memory bits. '''

generator_values = [x * 2 for x in range(100000)]
getsizeof(generator_values)
print("List:", getsizeof(generator_values))            # Output: List: 800984 bits

''' Important notes when dealing with generator the generator boject does count you the total numbers
since it does not store in memory. Far example, if you pass the generator in len() method it get an 
TypeError "generator has no len" let's check it out. '''

print(len(values))
# output: TypeError: object of type 'generator' has no len()
# We only can get access when iterate the generator.
