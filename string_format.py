# str.format() = optional method that gives users more control when displaying output

number = 1000
animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal,item))

print("The number pi is {:.3f}".format(number))  # this displays 3 digits after the decimal portion of the number
print("The number pi is {:,}".format(number))  # adds a comma
print("The number pi is {:b}".format(number))  # display the number as binary
print("The number pi is {:o}".format(number))  # display the number as octal
print("The number pi is {:X}".format(number))  # display the number as hexadecimal
print("The number pi is {:E}".format(number))  # display the number in scientific notation
