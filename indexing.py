# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "kievDevOps!"

if (name[0].islower()):  # Checks if the specified index is lower case, returning true or false
    name = name.capitalize()
    print(name)

first_name = name[:4].upper()
last_name = name[4:].lower()
last_character = name[-1]  # Reverse indexing

print(first_name)
print(last_name)
print(last_character)
