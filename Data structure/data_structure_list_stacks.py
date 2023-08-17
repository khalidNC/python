''' A stack represents a linear arrangement of data that adheres to the "Last In First Out" 
(LIFO) principle. This implies that the most recently added element to the stack is the first 
one to be removed.
You can visualize a stack as a pile of plates stacked on top of each other. 
The operations on a stack are similar to how you'd interact with such a pile of plates:
* Push: You can place a new plate on top of the stack.
* Pop: You can remove the top plate from the stack.
* To access the plate at the bottom, you must first remove all the plates stacked on top.
This mirrors the behavior of a stack data structure.

In Real world example is your browser, whenever you navigate to an new website
your browser keep your browseing session so when you click on the back-button it takes you to 
the previous webpage. 

Let's see how it works:
First start with an empty stack []
now let's say we are navigating the wesite number 1, then 2, then 3
now I clik on back-button, at this point browser removes the item on the top of the stack which is 3 here.
Then it redirects us the previous websites. 
Now let's say we click on the back-button a couple of times and it ends up with an empty stack. 
At this point the browser disables the back-button. 
This is how the stack works. '''

[1, 2, 3]
[1, 2]
[]


''' Now we see how stack work in Python. Basically we will use a list boject. 
So we are defining a variable and set into it an empty list.
Let's say we navigate the website number 1, so we are going to add itme in the list by append() method.
Then navigate 2 and 3'''

browser_session = []
browser_session.append(1)
browser_session.append(2)
browser_session.append(3)

''' Now print and see what we have in the stack. We get a list of three items as outpu [1, 2, 3]'''

print(browser_session)

''' Now let's say the user clicks on back-button so the browser remove last item. How should this do? 
use pop() method. This will remove last item 3. We can print the itme that is removed if we want. Just
print and see.

Now print the stack once again and can see 3 is removed from the list. It return [1, 2]. 
Now you need get back the user to the last item of the list, that mean you should use index.
So this will retunr last item of list. You can print this with a lebel "Redirect" for clarity. 
Print and it returns Redirect 2 which means, when user clicks on the back-button it redirects 
previous website which is number 2. '''

print(browser_session.pop())
print(browser_session)
print("Redirect", browser_session[-1])

''' Now we have to check either the stack becomes empty or not. So use if statement. 
Note: number zero 0, empty string "", empty list [] all are False value so if you apply 
not oparator before them it returns bool True. So code will be; '''

if not browser_session:
    print("Disable") 

''' This means when the list become empty print Disbale. 

Fanilly the codes comes. '''

browser_session = []
browser_session.append(1)
browser_session.pop()

if not browser_session:
    browser_session
print("Disable")
