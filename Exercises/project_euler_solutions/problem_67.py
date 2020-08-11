"""
problem 67
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'),
a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18.
 It is not possible to try every route to solve this problem, as there are 299 altogether!
 If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all.
 There is an efficient algorithm to solve it. ;o)
"""
example = """
    3
    7 4
    2 4 6
    8 5 9 3
"""

with open('triangle.txt', 'r') as f:
    ls = f.read()


def convert_to_list(string_):
    nums_ = string_.strip().split()
    new_list_to_nums_ = []
    sub_list = []
    i = 1
    for k in nums_:
        k = int(k)
        if i == 1:
            new_list_to_nums_.append([k])
            i += 1
            continue
        sub_list.append(k)
        if len(sub_list) == i:
            new_list_to_nums_.append(sub_list)
            sub_list = []
            i += 1
    return new_list_to_nums_

def max_sum_in(list_):
    list_.reverse()
    sum_ = 0
    for k in range(1, len(list_)):
        for i in list_[k]:
            f_sum = i + list_[k-1][list_[k].index(i)]
            s_sum = i + list_[k-1][list_[k].index(i)+1]
            list_[k][list_[k].index(i)] = sum_ = max(f_sum, s_sum)
        print(list_[k])
    return sum_


print(max_sum_in(convert_to_list(ls)))







