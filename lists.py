# list = used to store multiple items in a single variable

food = ["yakisoba", "strogonoff", "spaghetti"]  # list

food[0] = "sushi"  # changes the specified item into the new string

food.append("french fries")  # inserts a new item at the end of the list

food.remove("strogonoff")  # removes the specific item from the list

food.pop()  # removes the last element of the list

food.insert(0,"cake")  # inserts a new element in the specified location of the list

food.sort()  # sorts the list alphabetically

food.clear() # clears the list
 
print(food[0])  # prints the specific item of the list

for x in food:  # prints the entire updated list
    print(x)
