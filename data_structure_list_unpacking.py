''' There might be a time when we need to assign the multiple elements in the list to
multiple variables like; '''

numbers = [1, 2, 3]

first = numbers[0]
second = numbers[1]
third = numbers[2]


''' o not doing this manually assign every elements we can do the unpacking list like; '''

first, second, third = numbers    # This is exactly same as above 3 lines. Let's print and see.

print(first)
print(second)
print(third)

''' Note: we always have to same numbers of variables as elements in the list. Like if we 
do first, second = numbers this will give error. 
So what will happen when this list has lots of elements and we need to unpack some of them?
The solution is we will assing varibales for the elements we wnt to unpack and then will write 
another general variable with asterisk. '''

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

first, second, third, *others = list_of_numbers

print(first)
print(others)

''' If we want to get last number. '''

first, *other, last = list_of_numbers

print(first, last)
print(other)
