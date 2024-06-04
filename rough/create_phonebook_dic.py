'''
  1. We will ask user to input person's name and his/her phone numbers
  2. Then we will build a dictionaries out of it.
  3. Then from the dictionary we will print the name and phone numbers like a phonebook.
  4. Then will add a feature that lookup a name or serach a name in the phonebook. if name is not found in the phonebook the print some sms else print something else.
'''

# To execute this:
# We will write a couple of helper functions and a main function.

def main():
  phonebook = user_phonebook()
  print_phonebook(phonebook)
  lookup_name_in_phonebook(phonebook)


def user_phonebook():
  '''
    This function returns a dictionary with key value pair of name and their phone numbers,
    getting the info from the user's input.
    1. Created an empty dictionary fist and store in a accomulator variable phonebook.
    2. Now for single input: Get input name and phone numbers form the user and sote in separate variables, name & phone_number.
    3. Then put back the value(phone_number) into dictionary's(phonebook) key[name].
    4. Now run a while loop for the input value True. and if input name equal to empty, means user hit Enter then loop break.
    5. And finally return the dictionary.
  '''
  phonebook = {}

  while True:
    name = input("Enter name: ")
    if name == "":
      break
    phone_number = input("Enter phone number: ")

    phonebook[name] = phone_number

  return phonebook


def print_phonebook(phonebook):
  '''
    This function loop over the dictionary items and prints the key and value separately so that
    it becomes more readable.
  '''
  for key, value in phonebook.items():
    print(f"\n{str(key)} -> {str(value)}")


def lookup_name_in_phonebook(phonebook):
  '''
    Our phonebook is created by the user's input.
    1. Now this function will lookup a specific name in the phonebook, which user serch by input()
    2. If name is in the phonebook, put the value into a variable. then print the name and number
    3. else print, The name is not found.
    4. Now put the full step in a while loop for the condition True.
    5. The if user input 'No Thanks' then the loop breaks.
  '''
  while True:
    name = input("\nSearch by Name: ")
    if name == "No Thanks":
      break

    if name in phonebook:
      phone_number = phonebook[name]
      print(f"\n{name} -> {phone_number}")

    else:
      print(f"\n{name} is not found in the phonebook")



if __name__ == "__main__":
  main()