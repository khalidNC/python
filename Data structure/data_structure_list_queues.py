'''  A queue represents a linear arrangement of data that adheres to the "First In First Out" 
(FIFO) principle. This implies that the most primerily added element to the queue is the first 
one to be removed. 

The real world example is a queue in a bank, the first person in the queue will be served
at first. 

Let's say we have a queue(list) of 3 items and you want to remove the first item first then
second the third. Note: when we remove first one the other items to be moved to one step ahead,
So if the list ha too many items like thousands items then all the thousands items are needed to
be moveded in momory if I remove first one. In this scenario, this is more afficent to use
deque object. '''

[1, 2, 3]
[2, 3]
[3]
[0]


''' Let's see how to use deque. So first we need to import deque from collections module.
Then define a variable let's say queue and send an empty list in deque object.
Now we need to add item in the deque object by append() method as we did for list object 

Now we can print and check if list is populated.
Then we can remove the first item form the queue witht popleft() method. Note:
This popleft() method is availabe for list objevt in python. '''

from collections import deque


queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
print(queue)

if not queue:
    print("Empty")
    