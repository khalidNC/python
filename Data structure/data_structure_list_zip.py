''' The zip() is a Python built-in method that combine multiple lists and return list of tuples. 
Syntax is, zip(list1, list2) => return zip object which is iterable, need to convert this in list
with list() method. that returns list of tuples, [(), (), ()]. '''

list1 = [1, 3, 5, 6, 8]
list2 = [2, 4, 7]

print(list(zip(list1, list2)))


''' Let's have another example. '''

list_1 = ["a", "b", "c"]
list_2 = [2, 3, 4]
list_3 = [5, 6, 7]

print(list(zip(list_1, list_2, list_3)))


''' The zip() function takes one or more iterables. So we can pass stirng, tuple, etc 
let's have a try. '''

list4 = [9, 8, 7]
list5 = [12, 13, 14]

print(list(zip("abc", list4, list5)))

# Tried with tuple
print(list(zip(("1", "2"), list4, list5)))
print(list(zip((1, 2), list4, list5)))
print(list(zip(("z", "y"), list4, list5)))

# Tried with set
print(list(zip({"Opu", "Nameera"}, list4, list5)))

# Tried with dictionary this returns key, so if want value the use .values()
print(list(zip({"Name" : "Opu", "Daughter" : "Nameera"}, list4, list5)))
print(list(zip({"Name" : "Opu", "Daughter" : "Nameera"}.values(), list4, list5)))

# Tried with range
print(list(zip(range(0, 2), list4, list5)))
