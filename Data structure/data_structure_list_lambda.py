''' Lambda function is a one line anonymous function than can pass to other function. 
Lambda function can take any number of arguments, but can only have one expression.
the lambda syntax is, lambda parameters : expression 
The expression is executed and the result is returned. 
Let's have an example: add 10 to an argument and return result. '''

lambda a : a + 10           # Here, a is the argument and a + 10 is the expression
x = lambda a : a + 10       # Let's store in a variable x
print(x(3))                 # Now put the value of a 3 and print x. And get the output 13


''' Usages of lambda: 
Let's say we have a function that sort a complex list. 
The sort function that sorts a list that have taple with 2 items, and sort by numbers. 
Here we have the function and we just reference the function in the sort() method. '''

items = [
    ("Product1", 10),
    ("Product2", 3),
    ("Product3", 13),
    ("Product4", 7),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)


''' Now instead of this function we can use a lambda expression passing as key 
into the sort() method that can sort the list in the same way. We know the lambda 
syntax is, lambda parameters : expression
So we can write the expression as; lambda item : item[1] 
by writing lambda we are telling python to treat this a anonymous function.
Then as syntax; item is the parameter of the function and 
the expression; item[1] is telling item should return index 1 than mean number
in the items list.
Now this lambda function will do the same work as the function we write before to 
sort. 
Let's print items and check. '''

items = [
    ("Product1", 10),
    ("Product2", 3),
    ("Product3", 13),
    ("Product4", 7),
]

items.sort(key=lambda item : item[1])
print(items)
