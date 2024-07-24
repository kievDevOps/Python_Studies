# tuple = ordered and unchangeable collection used to group related data together

student = ("Kiev",23,"male")

print(student.count("Kiev"))  # Counts how many times the specified name appears
print(student.index("male"))

for x in student:  # prints all values
    print(x)

if "Kiev" in student:
    print("Kiev is here!")
