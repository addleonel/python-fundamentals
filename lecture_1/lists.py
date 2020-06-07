#Using list 
myList = ['one','two','three','four','five']

print(dir(myList))
print(type(myList))
print(myList)

# adiciona other element in the list
myList.append('six') 
print(myList)

#contar las veces que el elemento esta en la lista
print(myList.count('one')) 

myList.extend([['seven','eight','nine','ten']]) 
print(myList)

#remove the selected element
myList.remove('two')
print(myList) 

# it need a index and value(index-value)
myList.insert(1,'two')
print(myList)
myList.insert(len(myList),'eleven')
print(myList)

#change the values of index [0],[1],[2],[3]
myList[0] ='uno'
myList[1] ='dos'
myList[2] ='Tres'
myList[3] ='cuatro'
print(myList)

#check if there is the determinated value
print('cuatro' in myList)
print('doce' in myList)

#remove
myList.pop(0)
myList.pop(0)
myList.pop(0)
myList.pop(0)
print(myList)

print()
print(".........................................................")
print()
secondList=[1,2,3,4,5,6,6,6,6,7,7,7,8,8,8]
print(secondList)
print("counting how many numbers there is")
print("there is {0} four".format(secondList.count(4)))
print("there are {0} sixs".format(secondList.count(6)))
print("there are {0} sevens".format(secondList.count(7)))
print("there are {0} eights".format(secondList.count(8)))

