from datetime import datetime, timedelta


# Past datetime
dt1 = datetime(2022, 10, 21) + timedelta(days=1, seconds=5000)

# Curent datetime
dt2 = datetime.now()

# print(dt1, dt2)

duration = dt2 - dt1
print(duration)
#OutPut: 361 days, 16:26:34.715323

# datetime attributes
print("days:", duration.days)
print("Seconds:", duration.seconds)
# OutPut: days: 361 Seconds: 59390

# datetime method .total_seconds()
print("Total Seconds:", duration.total_seconds())
# OutPut: Total Seconds: 31249967.450096

# Compare duration
if duration > timedelta(days=350, weeks=1):
  print("Duration is more than 350 days.")


''' The timedelta class is part of the datetime module in Python and represents a duration 
or difference between two dates or times. It allows you to perform arithmetic operations 
with dates and times. timedelta objects are often used for tasks like adding or subtracting 
time intervals from datetime objects. 

There is a class timedelta in datetime module, 
1. Let's start with importing them.
2. Now we created a couple of datetime objects dt1, and dt2 both return datetime but one 
   is current datetime another is past datetime.
3. Now when we subtract these 2 datetime then we get timedelta object. Line: 12-14
4. Timedelta object has few interesting attributes - .days .seconds
5. Also there is a method .total_seconds() this is not attribute this is a method.
6. Now we can also add a timedelta object to a datetime object. For example, let's add 
   timedelta 1day to our dt1 object. Here we can supply argument as integer like timedelta(1)
   1 is number of day. but for the clarity we better use keyword= arguement like timedelta(days=1)
   See line-5. 
7. We can also compare duration. For example here the duration = 360 days, 15:17:15.230268
   and we compare lile if it is greater or equal to somepoint or not. See line: 25-27 '''
