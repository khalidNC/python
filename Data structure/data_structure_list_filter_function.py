''' Here is another scenario on lambda function where we can use filter() a built-in function.
Let's we have a list of tuples with 2 imtes a string(product name) and a int(price). 
Now we want to get a list of items which product's price are more or equal to 10. 

So in basic way we can do;
define an empty list
then iterate the item in items and give the condition price more than or equal 10
then append to the empty list

But we can do the same thing in more alligant way in one line, using filter() funtion.
The filter() function syntax is, filter(func, iterable) and it returns iterable object.
So here we will pass lambda expression and the list(iterables) as arguments to the function. 
So lambda syntax we know, lambda parameter : expression
here the parameter is the item (in items) and the expresion is price so index[1] in the tuple
and the condition is the price should be equal or more than 10, so we can write item[1] >= 10
then the second argument is the iterable(the items list). 

Now define a variable(x) and assign the function to it and print x
it returns a filter object which is iterable. so either we can run for loops and print the list or
we can right way make the eiterable outcome a list using list() method.'''

items = [
    ("Product1", 3),
    ("Product2", 10),
    ("Product3", 12),
    ("Product4", 6)
]

prices = list(filter(lambda item : item[1] >= 10, items))
print(prices)
