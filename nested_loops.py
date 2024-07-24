# nested loops = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):  # outer loop
    for j in range(columns):  # inner loop
        print(symbol, end="")
    print()
