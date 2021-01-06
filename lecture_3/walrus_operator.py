
# Using The Walrus operator
# python 3.8+

# Syntax
# (any_variable_name := value)
# (number := 45)

# Example 1

# Without Walrus operator 
x = 12
value1 = x < 52  # value1 = true (Assignment)
print(value1)  # output true

# With Walrus operator
y = 3
print(value2 := y > 1)  # value2 = true (Assign and return the value) 
print(value2)


# Example 2

# Without Walrus operator
numbers = []
num = input("Type a number: ")
while num.isdigit():
    numbers.append(int(num))
    num = input("Type a number: ")
print("Without walrus operator", numbers)

# With Walrus operator
numbers2 = []
while (num2 := input("Type a number: ")).isdigit():
    numbers2.append(int(num2))
print("With Walrus operator", numbers2)

# Example 3
# Without Walrus operator
base = 10
if base == 10:
    answer = input("Type your answer: ")
    if answer != "":
        print("Nice")

# With Walrus operator
if (base2 := 30) == 30 and (answer2 := input("Type your answer")) != "":
    print("Nice")
















