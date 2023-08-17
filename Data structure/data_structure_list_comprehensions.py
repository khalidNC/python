''' So far we learnt how to use;
1 - lambda function;        Syntax - lambda parameter : expression
2 - map() function:         Syntax - map(func, iterable) => returns map object which is iterable
3 - filter() function:      Syntax - filter(func, iterable) => returns filter object which is iterable 

Now we will wrtie a couple of example on map() and filter() functions then will re-write those in lits
comprehensions expression. '''

items = [
    ("Product1", 4),
    ("Product1", 12),
    ("Product1", 10),
    ("Product1", 7)
]

''' I want to get a list of item with all numbers only. So we are mapping the list.'''

prices = list(map(lambda item : item[1], items))
print(prices)

''' Now I want to get item in the list but filter with the numbers which are greater equal to 10. '''

prices_more_than_ten = list(filter(lambda item : item[1] >= 10, items))
print(prices_more_than_ten)


''' Now we will re-write this with another Python expression called list comprehenssions;
The comprehensions syntax is, [expression, for item in list]

So instead of list() method we will just use squire brackets[]. 
Then at first, we will write the expression within the brackets. Here the expression is, we want
to get back the numbers only, so item[1]. 
and instead of map() & filter() methods we will do the for loop for item in list.
Let's try it out and see this gets the same results or not. '''

prices_comprehension = [item[1] for item in items]
print(prices_comprehension)

''' Now for the second example; we are not mapping we are just filtering. So
we actually want to get the item so our expression is item and then for item in the list
and the conndition is we want to get the item greater equal to 10. so we can write this with if 
statement. Let's try to write. '''

price_ten_comprehension = [item for item in items if item[1] >= 10]
print(price_ten_comprehension)
