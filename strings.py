# Text in the code surrounded with quote is string.
# We can use either double quote or single quote
# Also python allows to use tripple quote for the long text or text-block or multiple lines

course_python = "Python programming"
course_python_programming = 'Python programming'
course_with_khalid = "Khalid's Python programming"
course = 'Python programming on "Content aggregation" with Khalid'
message = """
Hello Mac,

This is Khalid form Bangledesh.

Thanks
"""

# Python built-in function to get the length of a string, means the number of characters in the string.
'''
What is is function - function is a reusable piece of codes that carries out a task. 
Python has built in set of functions that we can use to perform various task.
'''
print(course_python)
print(course)
print(len(course))

#Index, the position of each characters in the string
print(course_python[0])    # 0 indicates the first character
print(course_python[3])
print(course_python[-1])   # negative indexing -1 indicates the first character from the last
print(course_python[0:3])  # slice a string, this will return the characters from first pisition to third
print(course_python[0:])   # common sense, from first to last
print(course_python[:3])   # common sense, first 3
print(course_python[:])    # common sense from first to last

# Escape character and escape sequence in python
python_language = "Python programing \"language\""
python = "Python is one of the most \npopular programming languages" # \n is used to make a new line
print(python_language)
print(python)

# String formatting
first_name = "Khalid"
last_name = "Hussain"
full_name = first_name + " " + last_name # this concatination is valid but there formatting can also be used
full_name = f"{first_name} {last_name}"  # f/F both can be used and get the same results as above concatination
print(full_name)