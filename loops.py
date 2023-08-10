''' There are times that we need to repeat a task a number of times there we use Loop to create repeatation.
The range() function returns a sequence of numbers, starting from 0 by default,
and increments by 1 (by default), and ends at a specified number. '''

# Repeat a task for loop with range
for number in range(4):
    print("For loops attempt")

''' Here the number is integer so let's pass another argument in the print function 
that prints the number starting form zero '''
for number in range(4):
    print("For loops attempt", number)

''' Let's have some fun; adding one with the number'''
for number in range(4):
    print("For loops attempt", number + 1)

''' Now apssing another argument number multiply by a string a string '''
for number in range(4):
    print("For loops attempt", number + 1, (number+1) * ":")

''' As we can see the range function generate number starts from zero all the way upto the number
in range as argument but does not include the serial number. Let's pass another argument, say start from
1, and end on 5 and remove the "+ 1" from the number in print function. And that breings the same 
results as above. More cleaner codes.'''

for number in range(1, 5):
    print("For loops attempt", number, number * ":")

''' We can also pass third argument. The range() function defaults to increment the sequence by 1,
however it is possible to specify the increment value by adding a third parameter: range(1, 10, 2): '''
for number in range(1, 10, 2):
    print("For loops attempt", number, number * ":")

''' For else: 
The else keyword in a for loop specifies a block of code to be executed when the loop is finished: 
Let's have an example: imagine a scenario where after the first attempt we can send a message successfully
in this case loop will break after the successful message. If we do not break the loop will 
continue and will keep print 5 times.
Now what will happen if after 5 attempt still the sending message is not successfull. So we use else
statement for the loop. Else statement will execute after loop is done without breaking.
so diclear a variable successful_message and set it True or False. When it is True then the loop
will break and sending message successful and else block will not execute. When it is False then
full loop execute alose else statement will be xexcuted. '''

sucessful_message = True
for number in range(5):
    print("Attempt")
    if sucessful_message:
        print("Message is sent succesfuly afert first attempt")
        break
else:
    print("Attempted 5 time and message is failed")


''' Nested loop: keeping a loop inside another loop is called nested loop. the logic is
the "inner loop" will be executed one time for each iteration of the "outer loop":'''
for x in range(5):
    for y in range(6):
        print(f"({x}, {y})")

# Another example, takes lists of fruits and their traits
traits = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in traits:
  for y in fruits:
    print(x, y)
