name = input("What is your name?: ")

age = int(input("How old are you?: "))
age = str(age)  # This line changes the age variable from an integer to a string, so it can be put together with the other strings to be printed.

height = float(input("How tall are you?: "))
height = str(height)  # This line changes the height variable from a float to a string, so it can be put together with the other strings to be printed.

print("Hello "+name)
print("You are "+age+" years old.")  # The change in data type could also be done like this: +str(age)+
print("You have "+height+" m.")  # The change in data type could also be done like this: +str(height)+
