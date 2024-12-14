def my_generator(start, end):
    while start <= end:
        yield start  # Yield the current value.
        start += 1

# Using the generator
for value in my_generator(1, 5):
    print(value)
