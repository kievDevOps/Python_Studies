# nested functions calls = function calls inside other function calls
# innermost functions calls are resolved first
# returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ")  # input that will give value to the variable
#num = float(num)  # changes the variable from a string to a float
#num = abs(num)  # finds the absolute number
#num = round(num)  # rounds the value whitin the variable to the nearest number
#print(num)  # prints the result of these operations

print(round(abs(float(input("Enter a whole positive number: ")))))
