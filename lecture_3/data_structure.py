# I'm going to use list and the methods
from collections import deque
import math
from fundamentals.Class_3_MoreControlFlowTools.lambdaFunction import validation_INT as vint
# creating a empty list
lst_ONE = []
# creating a list with items

lst_TWO = [1, 2, 3, 4, 5, 6]
lst_TWO.append(12)
print(lst_TWO)
lst_TWO.extend([13,14,15,16])
print(lst_TWO)
lst_TWO.remove(2)
print(lst_TWO)
print(lst_TWO.pop(0)) # remove the item with position (x) and return this item
print(lst_TWO)
print(lst_TWO.index(13))
lst_TWO.insert(7, 15)
lst_TWO.insert(7, 15)
print(lst_TWO)
print(lst_TWO.count(15))
# reverse the list
lst_TWO.reverse()
print(lst_TWO)

# other list
lst_THIRD = [{"name":'Tom', "age":20, "city": 'california'}]
print(lst_THIRD)

print("-"*30)
# USING LISTS AS STACKS (PILAS)
print("STACKS")
stack_ONE = [1, 1, 2, 3, 5, 8, 13, 21, 34]
print(stack_ONE)
stack_ONE.append(45)
stack_ONE.append(79)
stack_ONE.append(124)
stack_ONE.append(203)
stack_ONE.append(327)
print(stack_ONE)
stack_ONE.pop()
stack_ONE.pop()
stack_ONE.pop()
stack_ONE.pop()
print(stack_ONE)
print("-"*30)
# USINF LISTS AS QUEUES
# we need to import deque from collections
print("QUEUES")
queues = deque([1, 1, 2, 3, 5, 8, 13, 21, 34, 45])
print(queues)
queues.append(79)
queues.append(124)
queues.append(203)
queues.append(327)
print(queues)
queues.popleft()
queues.popleft()
queues.popleft()
queues.popleft()
queues.popleft()
queues.popleft()
print(queues)
print("-"*30)
# USING LISTS COMPREHENSIONS
# list of square
print("LISTS COMPREHENSIONS")
squares= []
for i in range(0,11,1):
    squares.append(math.pow(i, 2))
print(squares)
print(math.fsum(squares))
# the concise form
squaresConcise = [math.pow(x, 2) for x in range(11)]
print(squaresConcise)
print(math.fsum(squaresConcise))
# using the list comprehesion to sum the cube numbers
def cubenumber():
    n = vint("type a integer number: ")
    cubelist = [math.pow(x, 3) for x in range(n)]
    print(cubelist)
    suma = math.fsum(cubelist)
    print("the sum is", suma)


cubenumber()







