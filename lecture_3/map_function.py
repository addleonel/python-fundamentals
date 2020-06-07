# I'm going to use the function 'map()'
# 'map' mapped all element that is in a iterable such as lists [], tuples (), sets {}  
# REQUIREMENT
# require a function, our case 'example'
# require a list, in our caee 'my_list'
# SYNTAX
# map(function, sequence[, sequence, ...]) then to convert to list

# ->first step
# create a function that return some value
def example(value):
    return value*2
# ->second step
# create a list
my_list = [1, 3, 4, 5, 6, 7, 8]
# ->third step
# using map
map_value = map(example, my_list)
# to print first, I should to convert 'map_value' to a list
print(list(map_value))
# the output will be [2, 6, 5, 10, 12, 14, 16]

# other way to write the same process
# now I will use the lambda function
# With this I just will need one line of code
print(list(map(lambda x: x*2, [1, 3, 4, 5, 6, 7, 8])))
# the output will be [2, 6, 5, 10, 12, 14, 16]

# Add two list is map using lambda
numbers1 = [1, 2, 3]  
numbers2 = [4, 5, 6]  
# print in one line
print(list(map(lambda x, y: x + y, numbers1, numbers2)))
# the output is [5, 7, 9]

# List of string
ls = ['one', 'two', 'third']
result = list(map(list, ls))
print(result)
# the output will be [['o', 'n', 'e'], ['t', 'w', 'o'], ['t', 'h', 'i', 'r', 'd']]

a = [1, 3, 5, 7, 8]
b = [4, 6, 7, 9]
c = [3, 4, 5, 7, 5]
print(list(map(lambda x, y, z: x*2 + y*3 + z*4, a, b, c)))
        









