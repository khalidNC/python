''' The infinite loop is a loop that runs forever. So in the below code, if we change the while condition
to True(this True is always ture) and the loop will run forever. To jump out of it we need to break
the loop. After we get the input from the user we get the command make it lower() and 
if it is equal to exit loop break.
This code retruns the same results as we learned on while_loops.py file. '''

# command = ""
# while command.lower() != "exit":
#     command = input(">>>")
#     print("Return", command)

# command = ""
while True:
    command = input(">>>")
    print("Return", command)
    if command.lower() == "exit":
        break

''' In this program we no longer need to difine the command variable to set an empty string,
because we make the while statement condition set to True but in previous, the while 
statement we set the variable command != "exit '''