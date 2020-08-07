# In this section I am going to use the for 

sum=0
for i in range(1, 11):
    sum += i

print("the sum is: {0}".format(sum))

# using 'for' 
print ("other operation")
for i in range(1, 6):
    for j in range(1, i+1):
        print(i)
    print()
# using again
print("other function")
for i in range(1, 11):
    if i % 2 == 0:
        for j in range(1, i+1):
            print(i)
    else:
        print("it's odd")
    
         





        
