# Iterable data types
# Iterable String: when run for loop on a string this return all elements in stirng
for x in "Python":
    print(x)

# Iterable list: when run for loop on a list this return all elements in the list
for i in [46, 78, 90]:
    print(i)

# Iterable tuple: when run for loop on a tuple this return all elements in tuple
for t in (46, 78, 90, "tuple"):
    print(t)

# Iterable range: when run for loop on a range this return all elements within the range
for r in range(1, 8):
    print(r)

''' Iterable dictionary: when run for loop on a dict this return all keys elements of the dictionary but we
can retunr value as well by using .values() method '''

for d in {"name" : "khalid", "age" : 40, "address" : "DOHS"}.values():
    print(d)

# cleaner code:
my_dict = {"name" : "khalid", "age" : 40, "address" : "DOHS"}
for d in my_dict.values():
    print(d)

# we can also return key and value together by using .items() method
for x, y in my_dict.items():
    print(x, y)


# Iterable set: when run for loop on a set this return all elements of the set
for s in {"Name", "khalid", "age", 40, "address", "DOHS"}:
    print(s)
