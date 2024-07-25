# scope = region that a variable is recognized
# a variable is only available from inside the region it is created
# a global scope (available inside & outside functions)

name = "Kiev"  # global scope (available inside & outside functions as it's a global variable)

def display_name():
    name = "DevOps"  # local scope (available only inside this function as it's a local variable)
    print(name)

print(name)
display_name()
