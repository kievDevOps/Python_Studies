# for loop = a statement that will execute it's block of code a limited amount of times
# while loop = unlimited
# for loop = limited

import time

for i in range(10):
    print(i+1)

for i in range(50,100+1,2):  # the 3rd statement (2), makes it so that it adds 2 instead of one
    print(i)

for i in "KievDevOps":  # each letter whitin the string will be printed in a new line
    print(i)

for seconds in range(10,0,-1):  # range(starting_point,ending_point,counting)
    print(seconds)
    time.sleep(1)
print("Happy New Year!")
