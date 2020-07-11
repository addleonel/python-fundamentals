# I'm going to use list and its methods
from collections import deque
# creating a empty list
lst_one = []
# creating a list with items
lst_two = [1, 2, 3, 4, 5, 6]
lst_two.append(12)
print(lst_two)
lst_two.extend([13,14,15,16])
print(lst_two)
lst_two.remove(2)
print(lst_two)
print(lst_two.pop(0))  # remove the item with position (x) and return this item
print(lst_two)
print(lst_two.index(13))
lst_two.insert(7, 15)
lst_two.insert(7, 15)
print(lst_two)
print(lst_two.count(15))
# reverse the list
lst_two.reverse()
print(lst_two)

# other list
lst_three = [{"name":'Tom', "age":20, "city": 'california'}]
print(lst_three)

print("-"*30)
# USING LISTS AS STACKS
print("STACKS")
stack_one = [1, 1, 2, 3, 5, 8, 13, 21, 34]
print(stack_one)
stack_one.append(45)
stack_one.append(79)
stack_one.append(124)
stack_one.append(203)
stack_one.append(327)
print(stack_one)
stack_one.pop()
stack_one.pop()
stack_one.pop()
stack_one.pop()
print(stack_one)
print("-"*30)

# USING LISTS AS QUEUES
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








