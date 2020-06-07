# I'm going to use the regular expressions
"""
    The regular expressions


"""
import re
pattern = r"(string)+"
type_str = input("type something: ")
# value = re.match(pattern, type_str)
# print(type(value))
if re.match(pattern, type_str):
    print("matched")
