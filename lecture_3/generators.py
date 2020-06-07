# I'm going to use the generators

# I'm going to create a generator

def multiplies_of(n):
    initial = 1
    for k in range(100):
        yield initial*n
        initial += 1


for i in multiplies_of(5):
    print(i)
    
print(multiplies_of(5))

# other form to use a generator
generator = (k**2 for k in range(5, 23) if k%2 == 0)

print("-"*30)

def pair():
    initial = 1
    while True:
        if initial%2==0:
            yield initial
        initial += 1


print(pair())


