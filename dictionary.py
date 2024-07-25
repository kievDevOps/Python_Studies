#  dictionary = changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})  # Updates a dictionary
capitals.pop('China')  # Removes a key pair
capitala.clear  # Clears the dictionary

print(capitals['Russia'])  # This prints the value of the specified key
print(capitals.get('Germany'))  # Checks if the key exists in the specified dictionary
print(capitals.keys())  # Prints only the keys
print(capitals.values())  # Prints only the values
print(capitals.items())  # Prints both keys and values
