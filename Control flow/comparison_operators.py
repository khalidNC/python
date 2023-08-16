''' We use comparison operator to confirm value. '''

print(10 > 3)             # Returns True
print(10 >= 3)            # Returns True
print(10 > 30)            # Returns True
print(10 >= 30)           # Returns True
print(10 == 10)           # Returns True
print(10 == "10")         # Returns False
print(10 != "10")         # Returns True

# Comparison operator use in stirng

print("football" > "baseball")      # will return True because football is written before gether than sign
print("football" == "Football")     


''' will return False because every characters here has numeric presentation. 
So numeric value of "f" and "F" are not same'''

print(ord("f"))
print(ord("F"))


''' To check numeric presentation of "f" and "F" we call the method ord() and compaire these are not same '''
