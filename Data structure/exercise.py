from pprint import pprint


''' There is a common question that big companies ask in the interviews. Let's say 
we have a text and we need to find the most frequent character in the sentence. Let's
find the solution: '''

sentence = "This is a common interview question"

# Here we need the information like, the character which reapts most in the sentence.
# So we need 2 things basically, the charater itself and the frequency of the character which is a number, 
# so we can say the information is key:value. So the data structure would be dictionary. 
# Let's create an empty dictionary
char_frequency = {}

# Now we will loop over the sentence and keep the key:value to the dictionary
for char in sentence:
    # Check if the current character is not a space
    if char != " ":
        # If the character is not a space do next. Means space is ignored.
        if char in char_frequency:
            # Check if the character is in the dictionary
            char_frequency[char] += 1
            # if we have the character in the dictionary then increment the frequency(value) by 1
        else:
            char_frequency[char] = 1
            # Else set the frequency 1

# Now let's print the dictionary
print(char_frequency)
# Output: {'T': 1, 'h': 1, 'i': 5, 's': 3, 'a': 1, 'c': 1, 'o': 3, 'm': 2, 'n': 3, 't': 2, 'e': 3, 'r': 1, 'v': 1, 'w': 1, 'q': 1, 'u': 1}
# To make the output more readable there is a trick, pretty-print. 
# We need to import pprint class from pprint module at the top of the page
# Then instead print() use pprint(). This function takes keyword arguments 
# So here we pass width=1
pprint(char_frequency, width=1)

# Now we have the dictionary but this is not sorted, because a dictionary default unsorted.
# And dictionary can not be sorted. So we need to convert it to a tuple then sorted()
# We know to make a dictionary to tuple just call a function items()
# At this stage if you do the sorted() function the it can not be sorted unless you mention the expression
# So we use lambda expression. syntax: lambda argument : expression 
# Now if we print we can see the sorted key value lowest to biggest
# so if we want biggest to lowser value just pass another argument reverse=True
# Now define a variable and store and the print

sorted_dictionary = sorted(char_frequency.items(), key=lambda key_value : key_value[1], reverse=True)
pprint(sorted_dictionary)

# Finaly, if we print the first item by index then we get the result most frequent character and frequency.
print(sorted_dictionary[0])


# Another way to solve this with max() method
text = "This is a common interview question asked by employer"

# Convert the sentence to lowercase if uppper case if a matter of counting
text = text.lower()

# Now Create a dictionary to store character frequencies
character_frequency = {}

# Count the character frequencies we loop over the stirng
for character in text:
    if character != ' ':  # Ignore spaces
        if character in character_frequency:
            character_frequency[character] += 1
        else:
            character_frequency[character] = 1

''' Now, find the most frequent character:  we use built-in max() method. 
here, in the max() function we need to specify a custome function as key argument 
which is dictionary.get
This custom function takes each key in the dictionary as input and returns the value. 
Then the max() function finds the key with maximum value. So max() function can be writte like this,
max(iterable, key=iterable.get) '''
most_frequent_character = max(character_frequency, key=character_frequency.get)

# Now it retunrs the character with the maximum frequency if I print.
print(most_frequent_character)        # Output: the most frequent character is "e"


''' Now we want to print the frequency. Here, the frequency is the value. We know if I print the iterable[key]
this will return value. So If I print the most frequent character as key then it return value of 
the character means the frequecny. So let's print the frequency. '''

print(character_frequency[most_frequent_character])

''' We get output: e 6
Let's put a label while print so that it is more readable. '''

print("Most frequent character is:", most_frequent_character)
print("And the frequency is:", character_frequency[most_frequent_character])



# Another way to solve this with for loop:
paragraph = """A generator expression in Python is a compact and memory-efficient way to create an iterator. 
It's similar in concept to a list comprehension or a dictionary comprehension, but instead of creating 
a list or dictionary, it generates values one at a time as you iterate over them. This is particularly 
useful when dealing with large datasets or when you want to avoid storing all values in memory at once."""

# Create a dictionary to store letter's frequencies, means key:value
letter_frequency = {}

# Count letter frequencies
for letter in paragraph:
    # Check if there is space, line break, etc and ignore
    if letter != " " and letter != "\n" and letter != "'" and letter != "," and letter != "-" and letter != ".":
        # check if the value or the frequency in the iterable then increase by 1
        # Else keep in the dictionary
        if letter in letter_frequency:
           letter_frequency[letter] += 1

        else:
            letter_frequency[letter] = 1

pprint(letter_frequency)

''' Now we want another for loop over the dictionary to get key: value. We know items() method
returns key value. it is unpcking tuple. '''

most_frequent_letter = ""
# deifne a variable innitially empty string to set the most frequent letter later
maximum_frequency = 0
# deifne a variable innitially empty int to set the total frequency later

for letters, frequencies in letter_frequency.items():
    # Check the each key(latters) and value(frequency) in the tuple
    if frequencies > maximum_frequency:
        # Check if frequencies is greater than zero
        maximum_frequency = frequencies
        # Set maxium frequency is equal to frequencies
        most_frequent_letter = letters
        # And set most_frequent_letter is equal to letters

# Then print with formating stirng and Output: Most frequent letter is: e and the frequency are 36
print(f"Most frequent letter is: {most_frequent_letter} and the frequency are {maximum_frequency}")
