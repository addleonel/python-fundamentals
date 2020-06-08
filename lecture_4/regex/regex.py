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
# match()        -- returns the first occurrence
# search()       -- returns a Match object if there is a math anywheter in the string
# findall()      -- returns a list all matches
# split()        -- returns a list where the string has been split at each match
# sub()          -- replaces one or many matches with a string

# using match function
list_urls = [
    'https://www.google.com',
    'http://coreyms.com',
    'https://youtube.com',
    'https://www.nasa.gov',
]
pattern_url = r'(https)://(www.)?([\w]+)\.([\w]+)'
for url in list_urls:
    url_matched = re.match(pattern_url, url)
    if url_matched:
        print(url_matched.groups())  # returns all groups in a tuple
        print(url_matched.group())   # returns the whole match
        print(url_matched.group(0))  # returns the whole match, same of group()
        print(url_matched.group(1))  # returns the first group
        print(url_matched.group(2))  # returns the second group
        print(url_matched.group(3))  # returns the third group
        print(url_matched.group(4))
        print(url_matched.start())  # where starts the match
        print(url_matched.end())    # where ends the match
        print(url_matched.span())   # returns a tuple (start, end)
        print(url_matched.string, type(url_matched.string))   # returns a string
        print('='*50)
    else:
        print('no match\n{}'.format('='*50))
else:
    print('proccess finished')
# using search() function
# Check if the string starts with "The" and ends with "Spain"
s = 'The rain in Spain'
pattern1 = r'^The.*Spain$'
r = re.search(pattern1, s)
if r:
    print("YES!")
else:
    print("NO")

list_emails = ['CoreyMSchafer@gmail.com',
                'corey.schafer@university.edu',
                'corey-321-schafer@my-work.net',
                ]
pattern_email = r'([a-zA-Z0-9_.+*-]+)@([a-zA-Z0-9_+*-]+)\.([a-zA-Z0-9_.+*-]+)'
for email in list_emails:
    email_matched = re.search(pattern_email, email)
    if email_matched:
        print(email_matched.groups())  # returns all groups in a tuple
        print(email_matched.group())   # returns the whole match
        print(email_matched.group(0))  # returns the whole match, same of group()
        print(email_matched.group(1))  # returns the first group
        print(email_matched.group(2))  # returns the second group
        print(email_matched.group(3))  # returns the third group
        print(email_matched.start())  # where starts the match
        print(email_matched.end())    # where ends the match
        print(email_matched.span())   # returns a tuple (start, end)
        print(url_matched.string, type(url_matched.string))   # returns a string
        print('{0}: {1} {2} {3} \t found a match\n'.format(email,email_matched.group(1),email_matched.group(2),email_matched.group(3)))
    else:
        print('{0}: {1} {2} {3} \t not match\n'.format(email,email_matched.group(1),email_matched.group(2),email_matched.group(3)))
else:
    print('proccess finished')
# using findall function
pattern2 = r'ai'
matched = re.findall(pattern2, 'The rain in Spain') # returns a list
print(matched)

# using split function
pattern3 = r'\s'
splitted1 = re.split(pattern3, 'we are the champions') # returns a list splitted
print(splitted1)
splitted2 = re.split(pattern3, 'we need just one day to improve with regex', 3) # returns a list splitted at the third space
print(splitted2)

txt = "The rain in Spain"
x = re.split("\s", txt, 2)  # Split the string at the first white-space character:
print(x)

# using sub function
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) #Replace the first two occurrences of a white-space character with the digit 9:
print(x)
