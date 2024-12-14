# Anonymous Function Example
# Using a lambda to square a number
square = lambda x: x * x

# Using lambda with a higher-order function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))

print("Square of 4:", square(4))  # Output: 16
print("Squared List:", squared_numbers)  # Output: [1, 4, 9, 16, 25]
