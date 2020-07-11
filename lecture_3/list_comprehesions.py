# USING LISTS COMPREHENSIONS
# list of square
import math

print("LISTS COMPREHENSIONS")
squares = []
for i in range(0,11,1):
    squares.append(math.pow(i, 2))
print(squares)
print(math.fsum(squares))
# the concise form
squaresConcise = [math.pow(x, 2) for x in range(11)]
print(squaresConcise)
print(math.fsum(squaresConcise))
# using the list comprehension to sum the cube numbers
def cube_number():
    try:
        n = int(input("type a integer number: "))
        cube_list = [math.pow(x, 3) for x in range(n)]
        # print(cube_list)
        s = math.fsum(cube_list)
    except ValueError:
        print("type a integer number")
    else:
        print("the sum is", s)


cube_number()