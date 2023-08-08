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

# String methods:
''' In Python, there are few functions that are specific to string. Python everything is object.
example, python_course is an object then put dot(.) after the object to get access to the set of python
built-in functions more accuratly these are called Method '''

python_course = "   Python language programming   "
print(python_course.upper())

''' This upper method return a new string of all capital letter by not affecting the original string.
If I print(python_course) that will return orignal string. and we can store the new string in a new variable '''

python_course_upper = python_course.upper()

python_course_lower = python_course.lower()
python_course_title = python_course.title()

print(python_course_lower)
print(python_course_title)

python_course_remove_space = python_course.strip()
print(python_course_remove_space)

python_course_remove_space_on_left = python_course.lstrip()
print(python_course_remove_space_on_left)

python_course_remove_space_on_right = python_course.rstrip()
print(python_course_remove_space_on_right)

# Find method return index
python_course_find_the_index_of_pro = python_course.find("pro")
print(python_course_find_the_index_of_pro)

#replace method
python_course_replace_p_with_k = python_course.replace("p", "k")
print(python_course_replace_p_with_k)

''' Use in oparator to find the existence of a character or a sequence of characters in string.
This will return boolean True/false '''
print("pro" in python_course)

''' This is an expression. Expression is a piece of codes that expresses the value '''

# Use not in oparator
print("pro" not in python_course)
