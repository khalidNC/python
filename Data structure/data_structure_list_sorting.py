''' Ascending order: rearranging list items with ascending order se use sort() method.
Example we have list of numbers that have no perticular order. '''

numbers = [1, 2, 5, 9, 0, 23, 54, 17, 12]
numbers.sort()
print(numbers)


''' Now we want to sort this decending order. The Sort() method has 2 parapeters 
key: and reverse: bool = True/False. So we can pass the reverse argument with bool True. '''

numbers.sort(reverse=True)
print(numbers)


''' These are basic of the sorting list. Now python has a built-in function sorted() we can 
do the same sorting as above with this method. This sorted() method the arument is 
iterable so you can send a list. The only difference is sorted() method will return
a new list but not modify the original list. '''

sorted(numbers)
print(sorted(numbers))


''' I can also pass another argument to make decending order reverse = True. '''

sorted(numbers, reverse=True)
print(sorted(numbers, reverse=True))


''' So sorting numbers and string are very easy but what if you have a liet of complex objects. For an example,
we have a tuple. Let's assume we are building an application that processing orders and we have list of order
items. Every items in the list is a tuple with 2 items product's name followed by price. 

Now if I going to sort() this and print nothing will change I will get same thing. Because Python does not 
how to sort this list. In this type of cases, we need to define a function to let pyhton work. '''

items = [
    ("Product1", 10),
    ("Product2", 3),
    ("Product3", 12),
    ("Product4", 7),
]

items.sort()
print(items)


''' Let's define a function sort_item 
and this function will take item(for this case a tuple), sort_item(item)
and should return a value of the item that will be sorted. 
let's say the price which index is 1 in the tuple. 
So if I return item[1] that mean it returns price.
Now python gets the numbers and can sort this by price. 

Now sort the items once again but we need to reference the function as argument of sort() method.
remember we are not calling the function, we are just referencing the function as argument 
of sort method so that python can understand now what to sort. '''

# items = [
#     ("Product1", 10),
#     ("Product2", 3),
#     ("Product3", 12),
#     ("Product4", 7),
# ]

# def sort_item(item):
#     return item[1]

# items.sort(sort_item)
# print(items)


''' Now let's print items 
but we get TypeError: sort() takes no positional arguments
that mean sort() method does not support the arguement with key= or reverse = bool
(when you place your cursor on the sort() method you can see this) 
so now set the argument key=sort_item
then print item and check this time it is sorted by price. '''

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

''' Exersise: 
1. Sort by index[0] which is string and see the result
2. Let's make some price same and then see the result
3. let's make it decending order as well '''
