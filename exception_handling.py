# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong :(")

else:
    print(result)

finally:
    print("This will always execute")
