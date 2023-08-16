'''' List is a built-in function in python. We use squire brackets to define a list 
with sequence of objects. So inbetween the brackets we can list string, integer, 
even list, and so on. and assign this to a veriable.'''

list_of_list = [["a", "b", "c"], [1, 2, 3, 5]]
letters = ["a", "b", "c"]
numbers = [1, 2, 3, 5]

''' Now we can do some tricks;'''
''' Let's say we have list of 100 zeros so we not need to manualy type 
all the zeros in the list. We can just put 1 zero in the list then multiply by 100. 
if you print the list you will get the list with 100 zeros'''

list_of_zeros = [0] * 100
print(list_of_zeros)


''' Let's concatinate lists with Plus sign: '''

concatinate_list = letters + numbers
print(concatinate_list)


''' Creating a list with built in function list(). Let's say we have to create a list with
number 0 to 20. So we can create the list as below: '''

list_creation = list(range(20))       

''' Here range(20) method returns 0 to 20 numbers, and list() method will create a list with it. 
let's print now and see. '''

print(list_creation)


''' Create a list with list() function with string "Hello World". '''

chars = list("Hello World")
print(chars)

''' This returns list of all characters. '''
