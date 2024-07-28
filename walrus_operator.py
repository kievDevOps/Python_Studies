# walrus operator :=
# assigns values to variables as part of a larger expression

print(happy := True)
# happy = True
# print(happy)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   food.append(food)
