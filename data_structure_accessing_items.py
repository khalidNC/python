''' To access itme in data like list we need to use squire brackets. '''

letters = ["a", "b", "c", "d"]
letters[2]
print(letters[2])

"So if want to print first item in the list index 0"
print(letters[0])

"If want to print last item in the list index -1"
print(letters[-1])

''' List is mutable means we can change or modify the itme inside the list. Let's modify
the 3rd index('c') to capital 'C' '''
letters[2] = "C"
print(letters)

''' Slicing the list, mean modified the list with the a range of numbers. The command is
with colon(:). Like i want to get a to c form the above list. So first index then colon
then the desire index within the squire brackets. 
Note: in slicing last index will be excluded, so if you want to print 3rd index then
you need to inclde the index. '''
print(letters[0: 3])

''' Now if you want to slice from the first index then you can also only wrtie the desire
index with colon. '''
print(letters[: 3])

''' Now if you want slice fron a index to last then just do the opsite as above. '''
print(letters[2:])

''' So if you want to get every other elements in the list. '''
print(letters[::2])

''' Let's have a better example, making a list with range of lat's say 20. So this will
return a list of numbers with 0 to 19. Now print this with [::2] to get every other numbers. '''

numbers = list(range(20))
print(numbers[::2])

''' Now if you want to return the original list with revers order then do [::-1] '''
print(numbers[::-1])
