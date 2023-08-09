''' There are times that we need to repeat a task a number of times there we use Loop to create repeatation '''

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
