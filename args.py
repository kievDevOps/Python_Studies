# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

def add(*stuff):
    sum = 0
    stuff = list(stuff)  # this changes from a tuple to a list, so it's changeable
    stuff[0] = 0  # this changes the value of the first index to 0, so instead of the sum being 21, it will be 20 as the value of 1 is equal to 0 now
    for i in stuff:
        sum += i
    return sum

print(add(1,2,3,4,5,6))
