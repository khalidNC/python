''' More examples of lambda expression. 
Map function is a built-in function that takes a lambda function and a itarable as parameters. 
map function syntax is, map(func, itarable) and we know lambda function is a function inside a function.
so it is, map(lambda parameters : expresion, itarable) iterable means, loops can run over the data. 

Let's say we have a list of taples with 2 items string(name of product), and int(price).
Now we want to modify the list and want to get a list of numbers excluding the string. 

The basic way to do this is, define an empty list e.g prices
then iterate over list of items(for loops) 
then add the price(int) to the prices list, so use append() method
then print the prices list, and you get the list of numbers. 
This how we transform the list to a new list.'''

items = [
    ("Product1", 8),
    ("Product2", 2),
    ("Product3", 6)
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)


''' But we can achive the same results in more allegiant way 
instead of the loop we can use map() function.
As we know map() function takes a func and iterable
so we use lambda function then iterable the items list
lambda syntax is lambda parameter : expression, so item is the parameter and item[1] index is the 
expression(we need to get the price(int).
Now let's define a variable for the map function to see what it returns.
And we do not need the loop anymore because the map() will do the same work, so we can delete loops.

Now let's print and check it returns map object which is also iterable. So we can do 2 things 
number 1, you can iterable the output for loop and get list. Number 2 you just use list() method 
to make the outcome a list. 

Now print and check it returns the same results as we did for loops. '''

items = [
    ("Product1", 8),
    ("Product2", 2),
    ("Product3", 6)
]

new_list_items = list(map(lambda item : item[1], items))
print(new_list_items)
