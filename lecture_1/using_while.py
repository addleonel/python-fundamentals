# using while loop
sum =0
n=153
while n>0:
    print("value of n: {0}".format(n))
    r=n%10
    print("resto: {0}".format(r))
    sum += r
    n=n//10
print("the sum is: {0}".format(sum))    
