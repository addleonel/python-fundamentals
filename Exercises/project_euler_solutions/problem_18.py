"""
problem 18:

"""
ls = """
    3
    7 4
    2 4 6
    8 5 9 3
"""
nums = """
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

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
            s_sum = i + list_[k-1][list_[k].index(i) + 1]
            list_[k][list_[k].index(i)] = sum_ = max(f_sum, s_sum)
        print(list_[k])
    return sum_


print(max_sum_in((convert_to_list(ls))))












