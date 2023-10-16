from datetime import datetime
import time


# Creating datetime object
dt1 = datetime(2023, 10, 16)
# dt = datetime(2023, 10, 16)
dt2 = datetime.now()
# dt = datetime.now()
dt = datetime.strptime("2020/01/20", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())

# dt.year
# dt.month
print(f"{dt.year}/{dt.month}")
#output: 2023/10

print(dt.strftime("%Y/%m"))
# Output: 2023/10

print(dt2 > dt1)
# OutPut: True


''' The datetime module in Python is a powerful module for working with dates and times. 
It provides various classes and functions for working with dates, times, and timestamps. 
The datetime module is part of the Python Standard Library and is commonly used in a wide 
range of applications that involve handling temporal data. 

1. Let's start with importing datetime class from datetime module on top. 
2. There are few ways to create datetime objects;
   a. datetime() class we pass year, month, day as argument and this return let's say dt object
   b. We can use .now() method to the datetime class. And this return current date time. 
   c. We use .strptime() method to parse or convert datetime string. This is usefull spicially 
      when we get input from a user or read from any file, in both scenario we dealing with string.
      And we can convert the string to datetime object. let's say we have string like "2020/01/20"
      So this string is the first argument, then we need to tell python that how we want to format, 
      which means we need to specify what parts represents year, month, day, time. And this is the 
      2nd argument as string. Here is all the formats: https://docs.python.org/3/library/datetime.html
   d. We can convert timestamp to datetime object. Let's import time module. Let's say we heve timestamp
      time.time() somewhere in our codes now we need to convert to datetime object. To do so we can call 
      datetime class method fromtimestamp() and pass the timestamp as argement. This retuns datetime object 
      same as others. 
3. Now, the datetime object has attributes like dt.year, .month, .day etc. So We can print(f"{}") with
   formatter string. line-15. 
4. We also have a method strftime() to format datetime. So we can call dt.strftime() this method is the 
   opposite strptime() here we convert string to datetime object. and strftime() convert datetime object into 
   a string. To do so we need to specify the directives(format) here strftime("%Y/%m") 
5. e can also compaire datetime objects. Like, if we change the first 2 object name dt1 and dt2. print '''


''' There are some other objects as well:
1. Creating date and time Objects:
2. Working with timedelta Objects: '''

# 1. Creating date and time Objects:
from datetime import date, time

# Step 1: Create a `date` object
some_date = date(2023, 5, 15)

# Step 2: Create a `time` object
some_time = time(14, 30, 0)

# Step 3: Print the `date` and `time` objects
print("Date:", some_date)       # OutPut: Date: 2023-05-15
print("Time:", some_time)       # OutPut: Time: 14:30:00


# 2. Working with timedelta Objects:
from datetime import datetime, timedelta

# Step 1: Create `datetime` objects for the current date and a future date
current_datetime = datetime.now()
future_datetime = current_datetime + timedelta(days=7)

# Step 2: Calculate the time difference
time_difference = future_datetime - current_datetime

# Step 3: Print the time difference
print("Current DateTime:", current_datetime)
print("Future DateTime:", future_datetime)
print("Time Difference:", time_difference)

# Output: Current DateTime: 2023-10-16 23:24:01.826819
# Output: Future DateTime: 2023-10-23 23:24:01.826819
# Output: Time Difference: 7 days, 0:00:00
