# We have a list of numbers
# Then we need to create a dictionary with the list items.
# The key will be the unique numbers in the list and the value will be the times of appearing the unique numbers

# num_list = [3, 4, 6, 7, 3, 9, 4, 3, 7]

# So the key value wii be like as:
'''
  3: 3
  4: 2
  6: 1
  7: 2
  9: 1
'''

def main():
  num_list = [3, 4, 6, 7, 3, 9, 4, 3, 7]
  counts = count_nums(num_list)
  print_counts(counts)


def count_nums(num_list):
  '''
    This is a helper function that returns the dictionary with key value pair. Where key will be 
    the unique numbers and the value will be how many times they appear in the list that already provided.
  '''
  # Fist we will create an empty dictionary
  # Then will check if the key of the dictionary is present in the list. If not present then set value equal to 1.
  # And if the key present then increased the value by 1.
  # Put the whole condition into a for loop with range of the list lenght. This is the way to run a loop over an iterable object.

  counts = {}

  for i in range(len(num_list)):
    num = num_list[i]

    if num not in counts.keys():
      counts[num] = 1
    
    else:
      counts[num] += 1
  
  return counts

# Now we want to a separate function to print the key value in more readable way
# It loop over the counts dictinary and print how many times the unique number are appear.
def print_counts(counts):
  for key in counts:
    value = counts[key]

    print(f"{str(key)} appears {str(value)} times")

'''
  Shortcut codes is:
  for key, value in counts.items():
    print(f"{str(key)} appears {str(value)} times")
'''



if __name__ == "__main__":
  main()