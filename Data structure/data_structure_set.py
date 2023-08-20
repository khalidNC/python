''' In Python, a set is an unordered collection of unique elements. This means that 
a set can't contain duplicate values, and the order of the elements is not guaranteed. 
Sets are often used when you need to store a collection of items without caring about 
their order and without allowing duplicates. 

For example we have a list of duplicate items and we want to make the list with unique item.
So we can convert the list to set(). '''

numbers = [1, 2, 2, 3, 3, 4, 7, 7, 5]

uniuqe_numbers = set(numbers)
print(uniuqe_numbers)     # the output is a set with unique numbres {1, 2, 3, 4, 5, 7}

''' Another example, we have a set and we can add, remove as we can do with list. '''

test_set = {1, 2, "test", 5, 4}
test_set.add("set")
test_set.add(6)
test_set.remove(6)
print(test_set)

# We can also get length of set
print(len(test_set))


''' So far these are basic of set. 
Now some powerfull mathematical usage of set. '''

# Union of two sets: Union returns a new set with all unique numbers from tow sets. expression: vertical bar |
first_set = {1, 2, 3, 4}
second_set = {3, 4, 5, 6}

union_set = first_set | second_set
print(union_set)                    # output: {1, 2, 3, 4, 5, 6}

# Altranatively we can use the buit-in method as well.
altranative_union_set = first_set.union(second_set)
print(altranative_union_set)


# Intersection of two sets: It returns a new set with the emements that are common. Expression: ampersand &
intersection_set = first_set & second_set
print(intersection_set)             # output: {3, 4}

# Altranatively we can use the buit-in method as well.
altranative_intersection_set = first_set.intersection(second_set)
print(altranative_intersection_set)


# Difference btween two sets: It exclude all common element and returs the difference. Expression: minus sign
difference_set = first_set - second_set
print(difference_set)

# Altranatively we can use the buit-in method as well.
altranative_difference_set = first_set.difference(second_set)
print(altranative_difference_set)


# Symmetric Difference: It returns all elements excetp the items in their intersections. Expression: ^ sign
symmetric_difference = first_set ^ second_set
print(symmetric_difference)         # Output: {1, 2, 5, 6}

# Altranatively we can use the buit-in method as well.
altranative_symmetric_diff_set = first_set.symmetric_difference(second_set)
print(altranative_symmetric_diff_set)


# Access item is set:
if 9 in first_set:
    print("yes")

else:
    print("No")


print(7 in first_set)       # This will print boolean True/False
