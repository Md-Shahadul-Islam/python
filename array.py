def infinite_array():
    index = 0
    while True:
        yield index
        index += 1

# Create an instance of the infinite array generator
arr = infinite_array()

# Use the next function to access elements from the infinite array
for i in range(20):  # For demonstration, let's print the first 20 elements
    print(next(arr))
