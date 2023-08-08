''' Almost every where in the program we need to make decision that's when we use an if condition. '''
# let's say we have an variable:

temparature = 35

''' And we want to display a message when the temparature is greater than 30, so we use an if statement.
after wriete 'if' need to put a condition which is basically a boolean expression - the expression
that produces boolean value. Example: if temparature > 30 here we have a boolean expression, if the expression
value is True then the following statement will be executed.
Note: when we use if statement the expression will be ended with a punctuation colon(:)'''

if temparature > 30:
  print("It's hot")         # there is 2space indentation, that implies these statements will execute under if.
  print("Drink water")      # As many as statements with the indentation will be executed
elif temparature > 20:      # We can use multiple if conditions as many as we need by elif
  print("It is nice")
print("Done!")              # There is no indentation so this statement is out of the if condition


''' let's have the temparature below 30, then following statements will not execute 
since the boolean expression return False. '''
temparature = 10

if temparature > 30:
  print("It's hot")         
  print("Drink water")
print("Done!")


''' Let's have the else condition now to excute other conditions '''
if temparature > 30:
  print("It's hot")         
  print("Drink water")
else:                             # If none of the if condition is Ture the use else condition
  print("It's cold")
print("Done!")


''' Technique to write cleaner code. and the Usage of Ternary Operator. '''
''' Let's assume we are writing a program for a office where the applicant's age must be less than or equal 30
else they will not eligible. '''

age = 28

if age <= 30:
  print("Eligible")
else:
  print("Not eligible")

# There is no problem with the above codes. But a cleaner way to achive the same result
if age <= 30:
  message = "Eligible"
else:
  message = "Not eligible"

print(message)

# Even more cleaner way. 
message = "Eligible" if age <= 30 else "Not eligible"
print(message)
