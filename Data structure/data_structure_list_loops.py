''' Here we will see how to loop over a list. '''

letters = ["a", "b", "c", "d"]

for letter in letters:
    print(letter)

''' If we want to get each index of this elements then we can use a built in
function called enumarate(). This will rertun taple(taple is a read only list can not modify) for each iteration. '''

for letter in enumerate(letters):
    print(letter)

''' Now if we print letter then you get taple, first item of the taple is index and second one is item of index. 
so now if you print letter by index 0 and 1 you get index and letters. '''

for letter in enumerate(letters):
    print(letter[0], letter[1])

''' Now we can unpack this taple as we unpack list. Here enumerate() returns taple for each itaration like 
(0, "a") os if we want to unpack we assing variable for each of them. like if we assing variable index, letter
so it looks like; '''

for index, letter in enumerate(letters):
    print(index, letter)
# This is exactlysame as the above.
