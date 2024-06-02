# List: There is a list numbers is provided. And we need to modify the list as [2, 4, 6, 8]

numbers = [1, 2, 3, 4]

# Using a for loop.
# Here in the loop, i is a variable, that everytimes changes it's value till the loop iterates
# i represents the index of the list: 0, 1, 2, 3 because the rnage function starts from 0.
# So if we store the value of list item index in variable(element_at_index). So everytimes i changes. For 0 index list item is 1, for 1 index item is 2.
# If we print element_index at this stage, we will get 1 2 3 4 since the loop runs 4 times and the list items are 1, 2, 3, 4
# Now we will update the  list items: element_index value are now changes from 1 to 4 while loop runs, so we can multiple them by 2 inside the loop. And store the value back into the list by index numbers[i]
# Now print the list means numbers. It will return the list updated with items 2, 4, 6, 8.
for i in range(len(numbers)):
  element_at_index = numbers[i]
  numbers[i] = 2 * element_at_index
  # print(numbers[i])
print(numbers)


'''
a shortcut way to print elements in the list:
'''
num = [1, 2, 3, 4]

#If we need to know the elements as well as their index then use the loop:
# for i in range(len(num)):
#   elem = num[i]
#   print(elem)

# If we need to know only the elements then use this loop:
for elem in num:
  print(elem)


'''
Get sum of numbers form a list:
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# This function take the list of numbers as parameter, and returns sum of them.
def sum_of_nums(nums):
  # Innitially the sum is o. this is a variable called accumulator variable. It changes the value in every iteration in the loop
  sum = 0

  # number is another variable that changes in every iteration, this represents the element in the list.
  for number in nums:
    # The sum increases by the element in every iteration 
    sum += number
  # Then the function returns the sum after loop ends
  return sum


# Store the return value form the function after it is beign called. And print the value.
total = sum_of_nums(nums)
print(total)


# 28 or 42 which one will be printed out of the below function?
# It will print 28. Because in Python integer/float/string are imutable not changable. here, n is pointing a new value of 42 but x, which value is 28 will not be chnaged.
def main():
  x = 28
  change_value(x)

  print(x)

def change_value(n):
  n = 42



# Now we are going to do the same thing with a list rather than a number.
# here, my_list and list both variable point to the my_list value [42, 28, 16]
# Now append function adds 42 at the end of the list this time. because in python list is mutable. 
def main():
  my_list = [42, 28, 16]
  append_list(my_list)
  print(my_list)


def append_list(list):
  list.append(42)
  # list = []





if __name__ == "__main__":
  main()