''' When we wnat to pass multiple parameters exactly we dod not 
know how many they could be in that case, we cna use a esterisk(*) before 
the parameter. '''

# def my_function(*subjects):
#     print("My favourite subject is " + subjects[0])


# my_function("Match", "Music", "Art", "History")

# Rewriting the codes as return function
def my_function(*subjects):
    return "My favourite subject is " + subjects[3]


favourite_subject = my_function("Match", "Music", "Art", "History")
# This way the function will receive a tuple of arguments, and can access the items accordingly
print(favourite_subject)


''' Let's have another example: we are going to multiply a set of number in numbers and 
get return the total. 

First define a fuction multiplication and pass parameter numbers since we do not exactly know
how many argumnets will be passed so I put asterisk before numbers.

Since we are going to multiply numbers for we are making a for loop. for number in numbers 
multiply numbers with the total. and initially the total is 1.

Now  just return the total. Annd call the function.

And store this is a variable get_total. Then we can do whatever with the variable,
like we can prin in terminal. '''

def multiplication(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


get_total = multiplication(2, 3, 5, 10)
print(get_total)

# Another example of addition
def addition(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


sum = addition(2, 3, 5, 0)
print(sum)


''' Arbitary keywords arguments. This is almost same as arbitary argument but here the 
function receive a dictinary of arguments. 

If we do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition. '''

def user_info(**users):
    print(users)


user_info(Id="001", name="Mac", age=22, address="New York")

''' Now if you run this program this will return the user info within a dictionary 
{'Id': '001', 'name': 'Mac', 'age': 22, 'address': 'New York'} 
Now we can get print of value of any keys in the argument. '''

def user_info(**users):
    print(users["age"])


user_info(Id="001", name="Mac", age=22, address="New York")


# Another example of function retrun value
def my_activities(**activities):
    return "Easiest activities are " + activities["cardiac"] + " and " + activities["hip_build"]


activity = my_activities(chest_build = "50 Pushup",  hip_build = "50 Standips", cardiac = "1hr walk")
print(activity)
