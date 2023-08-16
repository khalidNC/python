''' Findind index of a given object. '''

letters = ["a", "b", "c", "d",]
print(letters.index("b"))


''' This returns index 1 of letter "b". 
Now if we want to get index of an item that does not exist in the list. Suppose we try to get index
of letter "e", now if i print then I will get value error 'e' is not in the list. '''

# print(letters.index("e"))


''' output: ValueError: 'e' is not in list 
to avoid getting the error we can check if the object exist in the list or not, for this 
we use in oparator. And this time it is not giveing error. '''

if "e" in letters:
    print(letters.index("e"))


''' Another usefull method is count() that will return number of objects in the list. So for the item
that does not exist should return zero. let's try it out. '''

letters.count("e")
print(letters.count("e"))
