"""
problem 
"""
import math
def posibilities(to_number):

    for a in range(1, to_number):
        for b in range(1, to_number):
            for c in range(1, to_number):
                if c == math.sqrt(b**2+a**2):
                    p = a+b+c
                    if p == to_number:
                        yield a, b, c

def count_p(ps):
    c = 0
    for k in posibilities(ps):
        print(k)
        c+=1
    return c/2

def require(to):
    lt = []
    n = 1
    while n <=to:
        c = count_p(n)
        print(c)
        lt.append(c)
        n +=1
    return lt

print(max(require(1000)))
                    
                
