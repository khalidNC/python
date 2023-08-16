''' While loop is use to iterate loop as long as the condition is True. 
Let's have an example: Set a variable number and set a the vale 100
then set the condition while number is greater than 0 print some maths'''

number = 100
while number > 0:
    print(number)
    number //= 2   # We are floor diving the number by 2(same as: number = number // 2)

''' Look at the results this program returns;
100
50
25
12
6
3
1

So this while loop does not iterate over a iterable data(like str, int, ect) rather 
it evaluates the condition then repeat the task. '''

''' Let's have another real world example: when we write 'python' command on terminal and hit 
the enter button then we entered the python program.
and the program waits for nex command with pointing arrow >>> 
then we write next expresion like, 2 + 4 and hit enter then it returns 4.
So the python program never ends untill we command exit(). 
So behind the scene we have a while loop until input sxit(). 
So here is the condition close_python = exit that breaks the while loop. '''

''' Let's buid something like this in python;
Dfine a varibale command and set it to an empty string.
then we need a while loop to execute as long as the coomand does not equal to Exit.
the we need to get contius input from user. So we use the built-in function input().
And  we add a lable like ">>>" as input method argument(this arrow will display in the 
terminal to get input from user). then keep this in a variable command. 
Now print a text like Return and pass another argument command. so the users
can return back what they inter.
So this our while loop unitil we type Exit. '''

# command = ""
# while command != "Exit":
#     command = input(">>>")
#     print("Return", command)

''' Now we run the program and type anything and can get back this.
and when we type exactly "Exit" then the while loop terminate and we are
get out of the input command. 
But if we type "exit" or "EXIT" then the loop does not terminate. To solve this
we can use a built-in function .lower() so whatever case we type it convert to lower. '''

command = ""
while command.lower() != "exit":
    command = input(">>>")
    print("Return", command)
