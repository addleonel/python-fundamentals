# USING LISTS COMPREHENSIONS

# list of square
import math

print("LISTS COMPREHENSIONS")
squares = []
for i in range(0, 11, 1):
    squares.append(math.pow(i, 2))
print(squares)
print(math.fsum(squares))
# the concise form
squares_concise = [math.pow(x, 2) for x in range(11)]
print(squares_concise)
print(math.fsum(squares_concise))

squares_even_number = [k**2 for k in range(1, 20) if k % 2 == 0]
print(squares_even_number)
print(math.fsum(squares_even_number))

# cartesian product
cartesian_product = [(x, y) for x in range(1, 10) for y in range(1, 5)]
print(cartesian_product)

cartesian_product_ = [(x, y) for x in range(1, 10) for y in range(1, 5) if x == y]
print(cartesian_product_)

cartesian_product__ = [(x, y, z) for x in [1, 2, 3] for y in [5, 6, 7] for z in [6, 5, 2] if x + y + z >= 10]
print(cartesian_product__)


# using the list comprehension to sum the cube numbers
cube_list = [math.pow(x, 3) for x in range(20)]
print(cube_list)
print(math.fsum(squares_even_number))