# I'm going to use some looping techniques

dic = {'name': 'Newt', 'surname': 'Evanoc', 'age': '29'}

for k, v in dic.items():
    print('{0}: {1}'.format(k, v))

question = ['name', 'surname', 'favourite color']
answer = ['Newt', 'Evanoc', 'Green']

for q, a in zip(question, answer):
    print('What is your {}? -> {}'.format(q, a))

# range without reversed method
for i in range(1, 10, 2):
    print(i)

print('-'*30)
# using reversed
for j in reversed(range(1, 10, 2)):
    print(j)

print('-'*30)
# sort a list
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
nums = [3, 1, 23, 4, -4, 5, 9, 8, 7]
for i in sorted(nums):
    print(i)
    
for i in sorted(set(basket)):
    print(i)







 



















