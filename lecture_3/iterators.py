
class EvenNumbers:
    """
    This iterate even numbers
    """
    def __init__(self, max_):
        self.max = max_

    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        if self.number <= self.max:
            x = self.number
            self.number += 2
            return x
        else:
            raise StopIteration


def even_number_generator(begin, limit):
    """
    This is a sugar syntax of the above code
    """
    for k in range(begin, limit + 1):
        yield k


if __name__ == '__main__':

    for number in EvenNumbers(10):
        print(number)

    for number in even_number_generator(1, 7):
        print(number)

    my_list = [2, 3, 6, 4, 7, 8]  # an list is an iterable
    # How to iterate and iterator
    # Create an iterator
    my_iterator = iter(my_list)  # this is an iterator
    while True:
        try:
            element = next(my_iterator)
            print(element)
        except StopIteration:
            break

    # the sugar syntax for above code
    for element in my_list:
        print(element)
