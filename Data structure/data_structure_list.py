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

# Concatinate 2 lists of dictionaries:
data1 = [{"Question": "Question 1", "Vote": "1"}, {"Question": "Question 2", "Vote": "2"}, {"Question": "Question 3", "Vote": "3"}]
data2 = [{"Question": "Question 4", "Vote": "4"}, {"Question": "Question 5", "Vote": "5"}, {"Question": "Question 6", "Vote": "6"}]

data = data1 + data2
print(data)

# Output: 
# [{'Question': 'Question 1', 'Vote': '1'}, {'Question': 'Question 2', 'Vote': '2'}, {'Question': 'Question 3', 'Vote': '3'}, 
#  {'Question': 'Question 4', 'Vote': '4'}, {'Question': 'Question 5', 'Vote': '5'}, {'Question': 'Question 6', 'Vote': '6'}]