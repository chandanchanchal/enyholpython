class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # The object itself is the iterator.

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # End of iteration.

# Using the iterator
my_iter = MyIterator(1, 5)  # Create an iterator from 1 to 5.
for num in my_iter:
    print(num)
