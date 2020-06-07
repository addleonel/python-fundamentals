# read and write files use -> function open()
# manipulate paths use -> os.path module
# read all the lines in all the files on the command line see the -> fileinput module
# create temporal file and directories use -> tempfile module
# high-level file and directory handling -> shutil module

import os

# 
print(os.name)

# returns the Current Working Directory(CWD) of the file used to execute the code
print(os.getcwd())

file = os.open("file.txt", os.O_WRONLY)
os.write(file, str.encode("hello"))
os.close(file)

"""
# print(os.stat("../../"))
d = os.environ # return a dictionary
# for i in d.items():
#     print(i)

# get access of environment variables
# os.environ.get("<name_of_environment>")
print(os.environ.get("TEMP"))

# modify environment variable's value
# but any changes will be effective only for the current process 
# where it was assigned and it will not change the value permanently. 
# from
print("Value before:", os.environ.get("USERNAME"))
# to
os.environ["USERNAME"] = "Pedro2"
print("Value after:", os.environ["USERNAME"])

# add a new variable
os.environ["NEW_ENVIROMENT_VARIABLE"] = "C:\\ewvalue"
print(os.environ["NEW_ENVIROMENT_VARIABLE"])

# if enviroment variable doesn't  exist
# form 1
# where os.environ.get(<name_of_environment>,<message_if_the_value_from_the_environment_is_None>)
print("Value:", os.environ.get("NAME_ENVIRONMENT", "This environment variable doesn't exist"))
# form 2
# using try: ... except KeyError: ...
try:
    # if the enviroment variable doesn't exist raise exception, in this case KeyError
    print("Value:", os.environ["NAME_ENVIRONMENT"])
except KeyError:
    print("This environment variable doesn't exist")
    
#

"""








