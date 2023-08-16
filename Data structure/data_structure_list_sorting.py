''' Ascending order: rearranging list items with ascending order se use sort() method.
Example we have list of numbers that have no perticular order. '''

numbers = [1, 2, 5, 9, 0, 23, 54, 17, 12]
numbers.sort()
print(numbers)


''' Now we want to sort this decending order. The Sort() method has 2 parapeters 
key: and reverse: bool = True/False. So we can pass the reverse argument with bool True. '''

numbers.sort(reverse=True)
print(numbers)
