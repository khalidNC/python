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
print("Done!")              # There is no indentation so this statement is out of the if condition

age = 25

if age > 45:
  print('Go to retirement')
else:
  print('You still have time to work')