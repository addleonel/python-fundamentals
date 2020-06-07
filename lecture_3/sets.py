
# set
set_a = {1, 2, 3, 4, 5, 6}
set_b = {4, 5, 6, 7, 8, 9}

set_uni = set_a | set_b
set_ist = set_a & set_b
set_d_1 = set_a - set_b
set_d_2 = set_b - set_a
set_smt = set_a ^ set_b
# print
print("set a: {} \nset b: {}".format(set_a, set_b))
print("union: {}\nintersection: {}\ndirefencia1: {}\ndiferencia2: {}\nsimetrica: {}".format(set_uni, set_ist, set_d_1, set_d_2, set_smt))

