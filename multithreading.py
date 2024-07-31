# thread = a flow of execution, like a separate order of instructions
# each thread takes a turn running to achieve concurrency
# GIL = (global interpreter lock), allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
# use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
# use multithreading

import threading
import time

def eat_breakfest():
    time.sleep(3)
    print("You eat breakfest")

def drink_coffee():
    time.sleep(4)
    print("You drink coffee")

def study():
    time.sleep(5)
    print("You study")

x = threading.Thread(target=eat_breakfest, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

#eat_breakfest()
#drink_coffee()
#study()
