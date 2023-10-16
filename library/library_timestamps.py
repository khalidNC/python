import time


''' The time module in Python provides functions to work with timestamps, which represent points in time. 
It's commonly used for measuring and representing time intervals and for performing time-related operations. 
Timestamps are typically expressed in seconds since the "epoch," which is a predefined point in time. 

Python has a time module, so let's start with import time module on the top.
Here are few examples on the methods and functions that time module provides for working with timestamps:

1. time(): Returns the current timestamp in seconds since the epoch.
2. ctime(): Converts a timestamp to a human-readable string.
3. gmtime(): Returns a struct_time object representing the current time in UTC.
4. localtime(): Returns a struct_time object representing the current time in the local time zone.
5. mktime(): Converts a struct_time object to a timestamp.
6. sleep(seconds): Suspends the program execution for the specified number of seconds.
7. strftime(format, t): Formats a struct_time object as a string according to the specified format. '''


# 1. Get the Current Timestamp: this time module has method called .time() and it retunrs current timestamp
current_time = time.time()
print("Current Timestamp in seconds:", current_time)
# OutPut: Current Timestamp in seconds: 1697426380.477698
# Step 1: Use time.time() to obtain the current timestamp in seconds.
# Step 2: Print the obtained timestamp.
''' An example of timestamps how we can calculate time:
Suppose I am sending email to 10000 recipients. So I am difining a funtion send_emails().
then iterate over it for i in range(1000): pass. 
Then we call the function send_emails()
before that we store the current time in start_time variable
Then after the funtion called store end_time
Then deduct start_time from end_time and store the result in duration variable.
Then print duration and we get time that takes to perform the function, which is 0.0005838871002197266 '''

def send_emails():
  for i in range(10000):
    pass

start_time = time.time()
send_emails()
end_time = time.time()

duration = end_time - start_time
print(duration)


# 2. Converting Timestamp to a Human-Readable Format:
# Let's say we have a timestamp = 1633667600
# Then we define a variable
# Then pass this timestamp as argument in ctime() method
# And print and the output is human readable: Fri Oct  8 10:33:20 2021

timestamp = 1633667600

human_readable_time = time.ctime(timestamp)
print(human_readable_time)

# 3. Working with struct_time Objects:
# Step 1: Get the current time in UTC
utc_time = time.gmtime()

# Step 2: Print the UTC time as a struct_time object
print("UTC Time as struct_time:", utc_time)
''' Output: UTC Time as struct_time: time.struct_time(tm_year=2023, tm_mon=10, tm_mday=16, 
    tm_hour=10, tm_min=37, tm_sec=57, tm_wday=0, tm_yday=289, tm_isdst=0) '''

# Step 3: Convert the struct_time object to a timestamp
timestamp = time.mktime(utc_time)

# Step 4: Print the converted timestamp
print("Timestamp from struct_time:", timestamp)
# Output: Timestamp from struct_time: 1697431579.0

# Step 5: We can convert this to human readable. To do use ctime() method and pass the timestamp as argument
print("Timestamp human readable:", time.ctime(timestamp))
# Output: Timestamp human readable: Mon Oct 16 10:46:19 2023


# 4. Sleeping for a Specific Duration:
# Step 1: Sleep for 3 seconds

print("Before sleep")
time.sleep(3)  # Sleep for 3 seconds

print("After sleep")
# Output: When you run the program you may notice it waited for 3 seconds


# 5. Formatting Time:
# Step 1: Get the current time in a struct_time object
current_time = time.localtime()

# Step 2: Format the time as a string with a custom format
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

# Step 3: Print the formatted time
print("Formatted Time:", formatted_time)
# OutPut: Formatted Time: 2023-10-16 16:50:40

''' 
Step 1: Use time.localtime() to get the current time as a struct_time object.
Step 2: Use time.strftime() to format the time according to the specified format.
Step 3: Print the formatted time. '''
