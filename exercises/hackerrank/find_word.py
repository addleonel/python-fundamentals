
pattern = r'[a-zA-Z0-9_]+'
text = ''
c1 = 0
c2 = 0

for line in sys.stdin:
    text += line

match_ = re.findall(pattern, text)
print(match_)
if match_:
    for k in match_:
        c1 = match_.count(k)
        if c1 > c2:
            c2 = c1

sys.stdout.write(str(c2))
