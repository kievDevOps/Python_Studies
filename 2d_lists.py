# 2d lists = a list of lists

drinks = ["coffee", "coke", "wine"]
dinner = ["strogonoff", "pizza", "yakisoba"]
dessert = ["cake", "ice cream"]
food = [drinks, dinner, dessert]

print(food)  # prints the list containing the other lists
print(food[2])  # prints the specified list 
print(food[2][1])  # prints the specified item of the specified list
