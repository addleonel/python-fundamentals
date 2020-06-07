# I'm going to use the principal function of regex in python
# simple concept: is a sequence of characters that forms a search pattern
# To use regular expressions in Python you need to import the re module
# as the following:

import re

# METACHARACTERS -- DESCRIPTION         -- EXAMPLE
#======================================================================
#       []       -- A set of charecters -- "[a-m]" from a to m
#       \        -- special sequence    -- "\s"     space
#       .        -- any characters      -- "hiper...t"  three any characters
#       ^        -- start with          -- "^good"
#       $        -- end with            -- "morning$"
#       *        -- zero to more        -- "bye*"
#       +        -- one to more         -- "tac+"
#       ?        -- Zero or one         -- "one?"
#       {}       -- number of occurences-- "{5}" or "{2-4}" -> 2 or 3 or 4
#       |        -- either or           -- "yes|no"
#       ()       -- capture and group   -- "(abc)" this is a group

# FUNCTIONS      -- DESCRIPTION
# =====================================================================
# findall()      -- return a list all matches
# search()       -- return a Match object if there is a math anywheter in the string
# split()        -- return a list where the string has been split at each match
# sub()          -- replaces one or many matches with a string

# Check if the string starts with "The" and ends with "Spain"
s = 'The rain in Spain'
pattern = '^The.*Spain$'
r = re.search(pattern, s)
if r:
    print("YES!")
else:
    print("NO")
