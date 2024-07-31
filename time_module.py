import time

print(time.ctime(0))  # convert a time expressed in seconds since epoch to a readable string
print(time.time())  # return current seconds since epoch
print(time.ctime(time.time()))

time_object = time.localtime()  # local time
time_object = time.gmtime()  # UTC time
print(time_object)
local_time = time.strftime("%B %d %Y %H:%M:%S",time_object)
print(local_time)

#----------------------------------------------------------------

time_string = "31 July, 2024"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)

#----------------------------------------------------------------

time_tuple = (2024, 7, 31, 11, 9, 0, 2, 0, 0)  # (year, month, day, hours, minutes, seconds, day of the week, day of the year, dst)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple = (2024, 7, 31, 11, 9, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)
