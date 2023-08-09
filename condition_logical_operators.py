''' Python has 3 logical oparators and we use those to model more complex conditions. The operators are
"and", "or", "not" '''
''' Example: Let's imagine we are building a application to process a loan who have good income 
and good credit scores, so we set variables as boolean True/False '''

good_income = False
good_credit = True
student = True

# if good_income and good_credit:
#     print("Eligible")
# else:
#     print("Not eligible")

message = "Eligible" if good_income and good_credit else "Not eligible"
print(message)

''' So for 'and' operator both conditions should be True '''

message = "Eligible" if good_income or good_credit else "Not eligible"
print(message)

''' So for 'or' operator any one of the conditions should be True '''

message = "Eligible" if not good_income else "Not eligible"
print(message)

''' So the 'not' operator make the boolean value inverse, here good income is flase so the 'not'
operator makes it True and reurns Eligible '''

''' Let's assume more complex scenario for this loan the applicant must have at least one True between good income
or good credit scores, and the applicant can not be a student '''

# if (good_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

message = "Eligible" if (good_income or good_credit) and not student else "Not eligible"
print(message)

''' Notes: Python interpreter does the short circuit evaluation. This is the same concept as short circuite
break in electric devides. Like, when there is condition unmatch/match the python stop executing the if
and execute the else statements'''

''' Chaining comparison operators to make more cleaner code. Let's assume the applicant is eligibile when
their age is between 18 and 65 '''

age = 61

# if age >= 18 and age < 65:
#     print("Eligible and age is matched")
# else:
#     print("Not eligible due to age restriction")

# Cleaner code can be written as;
# message = "Eligible and age is matched" if age >= 18 and age < 65 else "Not eligible due to age restriction"
# print(message)

''' Even more cleaner codes can be written by modifying the expression, it is same as plain English or match.
The expression can be written as "18 <= age < 65" this is called Chaining comparison operators'''

message = "Eligible and age is matched" if 18 <= age < 65 else "Not eligible due to age restriction"
print(message)
