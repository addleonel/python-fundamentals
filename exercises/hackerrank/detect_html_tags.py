# DETECT HTML TAGS
# https://www.hackerrank.com/challenges/detect-html-tags/problem

# Some link to practice:
# https://hr-testcases-us-east-1.s3.amazonaws.com/722/input04.txt?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1612935160&Signature=Ikg943k%2FiTfoeKJn1Gt9I6SXnBQ%3D&response-content-type=text%2Fplain


import re
import sys

pattern = r'<([a-z1-9]+)[^<>]*[\w\s]*>'
raw_ = ''
result_ = ''

for line in sys.stdin:
    raw_ += line

match_ = re.findall(pattern, raw_)
match_ = list(set(match_))
match_.sort()
if match_:
    result_ = ';'.join(match_)
print(result_)

