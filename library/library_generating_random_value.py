import random
import string

# random():
# Generate random value between 0 to 1 by using random() method and store the value in a variable
random_numner = random.random()

# Then print the generated random number
print(random_numner)
# OutPut: 0.7980202068356855


# randint():
# Generating random integer between 3, and 9 as 2 arguments supply to randint() method
random_integer = random.randint(3, 9)

# Then print the generated number
print(random_integer)
# OutPut: 4


# choice():
# Define a list of choices
choices = ['Rock', 'Paper', 'Scissors']

# Make a random choice
random_choice = random.choice(choices)

# Print the choice
print(random_choice)


# choices():
# Create a list of food items
menu = [
          "Fried Rice", 
          "Chicken Fry", 
          "Beef Sizzling", 
          "Soft Drinks", 
          "Thai Soup", 
          "Prown Curry", 
          "Chile Chicken", 
          "Beef Chile", 
          "Fish and Chips", 
          "Salad"
        ]

# Call the choices() method to pick random 3 items at a time
three_items = random.choices(menu, k=3)
three_items = ", ".join(random.choices(menu, k=3))

# Print the three items
print(three_items)
# OutPut: ['Chicken Fry', 'Chile Chicken', 'Salad']
# OutPut: Beef Chile, Beef Chile, Salad


# Choices(): Generate random password
# Import string module. It retuns string depends on the defferent attributes of the method.
# Let's print a couple of them
# print(string.ascii_letters)
# OutPut: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(string.digits)
# OutPut: 0123456789
# print(string.punctuation)
# OutPut: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Use of stirng trributes that return stirng and store in avariable
str_random = string.ascii_letters + string.digits + string.punctuation
# print(str_random)
# OutPut: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# Call the choices() method to pick random 6 carachters and store in a varibale
random_six_char = "".join(random.choices(str_random, k=6))
print(random_six_char)
# OutPut: ['!', 'n', 'T', 'I', 'k', 'w']
# OutPut: <v%S\3 after using of .join() method it returns a string


# shuffle():
# Define a list of elements and store in a variable
elements = [1, 2, 3, 4, 5]

#Shuffle the list in-place
random.shuffle(elements)

# Print the elements
print(elements)
#OutPut: [4, 2, 5, 1, 3]


# sample():
# Define a population of elements
population = ['A', 'B', 'C', 'D', 'E', 'F']

# Sample 3 unique elements from the population
sample = random.sample(population, 3)

# Print the sample
print("Random Sample:", sample)
# OutPut: Random Sample: ['F', 'A', 'D']


''' The random module in Python is used to generate random numbers, sequences, and make random choices.
It provides various functions for working with randomness and is often used in simulations, games, and 
statistical applications. Here's a brief overview of some key functions and their descriptions:

  1. random(): Returns a random floating-point number in the range [0.0, 1.0).
      a. Let's start with improting random module on the top.
      b. This module has a method called random(), Generate a random floating-point number between 0 and 1
      c. Let's print the random(). The OutPut we get a floating point number: 0.7980202068356855
         and every time we run the program we get a different value.

  2. randint(): This method generats Random Integers between 2 numbers. So we need supply 2 arguments.
      a. Generated random integer between 3 to 9 with the method called randint() then stored it in a varibale.
      b. Then print the number. Every time we run the program we get random number between 3 to 9.

  3. choice(): This method takes a list/array and ramdomly picks one of the item in the array. 
      a. Let's create a list of choices
      b. Then use the method choice() to make a choice from the list items and store it is a variable
      c. Then print the generated choise.

  4. choices(): With the help of this method we can make mupltiple choices from a list. To do so, we need a
                list of items and pass the list as 1st argument in the method, and we need to tell the method
                how many choices I can pick by passing keyword argument like k=2 or 3 or 4 whatever.
      a. Let's create a list of food items and store it in a variable.
      b. We want to pick 3 foods item randomly so k=3 which is our 2nd argument in the method.
      c. Then use the method like this - choices(list_name, k=3) and store it value in a variable
      d. Then print the value.
      e. Note: we are getting a arry as output from the origin array. Suppose we want to get comma separated
         item not array. To do so, we can use join() method. See at line: 50
      f. Let's create random password with the choices() method. 
          i. If we create a list of integer or string whatever this will be limited. So better we import
             another module called string. This module has few interesting attributes. See line: 59-65
          j. Use of stirng atrributes that return stirng and store it in a variable.
          k. Then sall the choices() method to pick random 6 carachters and store in a varibale.
          l. But it returns a array of string with comma separated. So use "".join() method
          m. Now every time you run the program it will return a random 6 letters password.

  5. shuffle(): This method shuffle the list itmes that we pass as argument into the method.
      a. Create a list of elements.
      b. Use random.shuffle(seq) to shuffle the list in-place.
      c. Print the shuffled list. 
      
  6. sample(): This method retruns unique sample size, a list of string from a original list/array.
      a. So we need a list of elements
      b. Then we need to pass this list as first argument to the method
      c. Then we need say the sample size, by providing a number as second argument
      d. Then print the result. It should returns unique sample from the list of elements. '''
