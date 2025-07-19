# Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# This defines the start and end of the range
start = 1
end = 11

# Use the range function with those values
for i in range(start, end):
    result = number * i
    print(number, "*", i, "=", result)
