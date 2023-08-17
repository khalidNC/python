''' We will cover adding and removing items from list. '''

letters = ["a", "b", "c", "d", "e"]


''' Adding: if you want to add element in the list on the last position. The method
you shiuld use is append(). You can add the desire element then print ad see the element
is added. '''

letters.append("e")
print(letters)


''' Also you can add 1 element in any position in the list by using insert() method. For insert()
method, you nedd to pass 2 arguments one is index(in which position you want to insert, 
and 2nd one is the item. So let's try inserting "Alphabet" in the fisrt possition. 
Then print and check.'''

letters.insert(0, "Alphabet")
print(letters)


''' Now there is another way to add multiple items to the end of the list. To do so you
need to call extend() method. Extend() method adds the specified list elements 
or any iterable(list, tuple, set etc) to the end of the current list. Let's extend the
letters list by adding a list ["f", "g", "h", "i"] '''

letters_extends = ["f", "g", "h", "i"]
letters.extend(letters_extends)
print(letters)


''' Now try to extend a tuple ("j", "k", "l")'''
more_letters = ("j", "k", "l")
letters.extend(more_letters)
print(letters)


''' Removing: we can also remove items from the list. 
If we want removing item at the end of list then used pop() built-in method.
If we want to remove item from any specific position then mention the index in thne pop(). '''

letters.pop()
print(letters)

letters.pop(0)
print(letters)


''' Now we want to remove item but we do not know the index. In this case we will use 
remove() built-in method. For an example we have new list for letters and there are 4 "b" 
this remove method will remove the first "b" from the list. '''

new_letters = ["a", "b", "c", "d", "b", "e", "b", "b"]
new_letters.remove("b")
print(new_letters)


''' Now if you want to remove all the "b" form the list, then we have loop over the list 
and remove each list individually. '''

new_letters = ["a", "b", "c", "d", "b", "e", "b", "b"]
for letter in new_letters:
    new_letters.remove("b")
print(new_letters)


''' We have another way to delete item is called the "del statement",
so we can use the del new_letter[] and mention the idex of the item that you
want to delete. '''

del new_letters[-1]
print(new_letters)


''' Also you can delete a range of item form a list with del statement. '''

my_list = ["football", "baseball", "cricket", "tennis", "swimming",]
del my_list[1:3]
print(my_list)


''' Finally, if you want to remove all items in the list use clear() method. Then print
and get empty list. '''
my_list.clear()
print(my_list)
