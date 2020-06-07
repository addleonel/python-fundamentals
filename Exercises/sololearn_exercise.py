# military hour
# from 1:15 AM to 1:15
# from 1:30 PM to 13:30
# from 12:00 AM to 0:00
# from 12:00 PM to 12:00
import re

hour1 = '1:15 AM'
hour2 = '1:30 PM'
hour3 = '12:20 AM'
hour4 = '12:59 PM'

def to_military_time(hour):
    pattern = '([0-9]{1,2}):([0-9]{1,2})\s(AM|PM)'
    r = re.search(pattern, hour)
    print(r.groups())
    h = int(r.group(1))
    m = int(r.group(2))
    ampm = r.group(3) 
    if ampm == 'AM':
        if h == 12:
            h = 0
        return '{:02d}:{:02d}'.format(h, m)
    elif ampm == 'PM':
        if h < 12:
            h += 12  
        return '{:02d}:{:02d}'.format(h, m)
    
# print(to_military_time(hour1))
# print(to_military_time(hour2))
# print(to_military_time(hour3))
# print(to_military_time(hour4))


# Password validation
# the password is valid if:
# it has at a minimum 2 numbers
# 2 of the following of characters (!@#$%&*)
# and a length of at least 7 characters
# if the password pass the check output 'Strong' else output 'Weak'

pw1 = '@Hello$World19'
pw2 = 'PasswordWord19$#'
pw3 = 'LeTme!n'
pw4 = '@Hel2lo1$World9'
pw5 = 'Hello1World9'

def pw_validation(pw):

    pattern1 = '(.*[0-9]+.*[0-9]+.*)'
    pattern2 = '(.*[!@#$%&*]+.*[!@#$%&*]+.*)'
    search_numbers = re.search(pattern1, pw)
    search_chars = re.search(pattern2, pw)
    pw_lenght = len(pw)   
    if search_chars and search_numbers and pw_lenght >=7:
        return 'Strong'
    else:
        return 'Weak'

print(pw_validation(pw1))
print(pw_validation(pw2))    
print(pw_validation(pw3))
print(pw_validation(pw4))
print(pw_validation(pw5))
    
    

 
 
 
 

