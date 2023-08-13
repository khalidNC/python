''' Here we try find bug and fix in the program. We will run the program in 
debugging mode and run codes line by line abd find bug and then fix. 
We will also learn some inportant shortcuts command to run program. '''

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total = total * number
#     return(total)
    

# print(multiply(3, 4, 5, 6))

''' The above function we are muiltiplying numbers and return value. In these codes we are making
an indentation error on line 9. Now if I run the codes it will not return the cirrect results.
So we will run this in debugging mode and find the bug. '''

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return(total)
    

print("Start")
print(multiply(3, 4, 5, 6))

''' Now we need follow few steps in VScode editor:
Open the debugging mode
then create a Json file for the current file(the terget file for debugging)
We actually nothing to do with json file, so close it.
Now we need to put a break point in code, so I place my cursor in line 19
and insert a break point by pressing fn + F9 on my Mac keyboard. 
The line is selected pointing a red dot. If I wnant to remove the pointing do same fn +F9.
Now we have to run the program up to the line 19. So I press fn + F5 to run.
Then the program runs upto the break point which ia highlighted.
Now we will run line by line and try to find what exactly happens.
So press fn + F10 to run next statement.
This way we repeat and run by pressing fn+F10
but we can notice the for loop does not continue the iteration. but it sould iterate
4times. it multiply first number-3 with the total(line21) which is innitially 1 
and return 3. Then the program get out of the loop.
Now we stop the debugging and space back the indentation for loop function
and run debugging again and see this time it return the results corretcly. '''
