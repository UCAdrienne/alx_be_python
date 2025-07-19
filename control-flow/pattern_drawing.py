# Prompt user to input size of pattern
size = int(input("Enter the size of the pattern: "))

# Definee the variable row which is counts the rows
row = 0
col = 0

# While loop to iterate through each row
while row < size:
    for col in range(size):
        print("*", end="")
    print()
    row += 1
