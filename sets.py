# set = unordered and unindexed collection, with no duplicate values.

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")  # add elements to a set
utensils.remove("fork")  # remove elements from a set
utensils.clear()  # clears a set
utensils.update(dishes)  # updates a set with another set
dinner_table = utensils.union(dishes)  # creation of a new set by the union of other sets

#print(dishes.difference(utensils))  # shows the different elements between the chosen sets
#print(utensils.intersection(dishes))  # shows the common elements between the chosen sets

for x in dinner_table:
    print(x)
