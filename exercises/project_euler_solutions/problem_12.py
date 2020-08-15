

def generate_triangle_numbers():
    # 
    n = 20050
    nd = 0
    while True:
        i = int(n*(n+1)/2)
        # print(i)
        for j in range(1, i+1):
            if i % j == 0:
                nd += 1
        yield i , nd
        print(i, nd)
        nd = 0
        n += 1
 
def over_to(num):
    
    for k in generate_triangle_numbers():
        if k[1] > num:
            print("-"*30)
            print(k[0])
            break
            
over_to(500)

