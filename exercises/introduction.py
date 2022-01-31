import math

def principalOperations():
        initial = int(input("the initial number: "))
        final = int(input("the final number: "))
        num_pair =[]
        num_odd = []
        letter =""

        for num in range(initial,final +1): 
                if(num%2==0):
                        num_pair.append(num)
                        letter ="pairnumber"
                else:
                        num_odd.append(num)
                        letter ="oddnumber"

        count =0
        lists = [2,2,3,34,34,56,[23,332]]
        for element in lists[0:4]:
                count +=1
                print(str(element)+", ")
        print("there are "+str(count) +" elements")
        print(num_pair)
        print(num_odd)
        print(letter[0:5])
        print(math.e)
        

# print lines that you want
def printLine(num):
        iterator =0
        print()
        while iterator<=num:
                print("-", end="")
                iterator +=1
        print()

def fibonacciSeries_1():
    print("Fibonacci series")
    a,b =0,1
    while a <50:
        print(a, end=" ") #end ="" this function is for print in the same text line
        a,b =b,a+b


def fibonacciSeries_2(num_1):
    print("Fibonacci series")
    a,b =0,1
    while a <num_1:
        print(a, end=" ") #end ="" this function is for print in the same text line
        a,b = b,a+b

def printList():
        myList = ["one", "two", "three", "four", "five"]

        for i in range(len(myList)):
                print(i+1, myList[i])


def fibonacciSeriesSetting():
        num = int(input("print a number to print the fibonacci number: "))
        fibonacciSeries_2(num)

if __name__ == '__main__':
    # the results
    fibonacciSeries_1()
    printLine(40)
    printList()
    printLine(60)
    fibonacciSeriesSetting()
