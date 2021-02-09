# DETECT HTML LINKS:
# https://www.hackerrank.com/challenges/detect-html-links/problem

# Some files to test the pattern:

# https://hr-testcases-us-east-1.s3.amazonaws.com/725/input03.txt?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1612849589&Signature=TBGIBogqTsgb0LsEnJyPT23hlow%3D&response-content-type=text%2Fplain

# https://hr-testcases-us-east-1.s3.amazonaws.com/725/input05.txt?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1612849082&Signature=DSChMEdeIIAorvUWtMA4OgA5PiU%3D&response-content-type=text%2Fplain

# https://hr-testcases-us-east-1.s3.amazonaws.com/725/input03.txt?AWSAccessKeyId=AKIAR6O7GJNX5DNFO3PV&Expires=1612848457&Signature=SdxiM4btI1Tk%2FRy5KVWPfXKkDJA%3D&response-content-type=text%2Fplain

import re
import sys

pattern = r'<a href="([^"]*)"[^<>]*>(<img.*/>)*(<[a-z]+>)*([a-zA-Z0-9\s\.,\/]*)(<\/[a-z]+>)*<\/a>'

html_ = ''

for line in sys.stdin:
    html_ += line

match_ = re.findall(pattern, html_)

if match_:
    for block in match_:
        sys.stdout.write(f'{block[0].strip()},{block[3].strip()}\n')
