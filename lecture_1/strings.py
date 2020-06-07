
#using strings
myString ="my time is longer"
myInteger= 23
int =455
print(int)

print(myString.upper()) #all in capital letters
print(myString.lower()) #all in lowercase
print(myString.capitalize()) # the first letter is in capital letter
print(myString.swapcase()) #change all in capital letters because the original string is in lowercase

print(myString.count('i')) #count 'i'

print(myString.replace('time', 'computer')) #replace 'time' by 'computer'

print(myString.startswith('me')) #this return a boolean, in this case 'false', because the inicial word 
                                  #of the text is 'my'
print(myString.endswith('longer')) #this return a boolean, in this case 'true', because the final word 
                                    #of the string or text is 'longer'

print(myString.split(' ')) #this split or separates the string according to ' ' it's a empty in this case
print(myString.split('i')) #this split or separates the string according to 'i'
print(myString.find(' ')) #this counts the string from the first letter to find the indicated character,
                            #in this case ' ' and value that return is 2
print(myString.find('o')) #This count the string from the first letter ti find the indicated character 
                            #in this case 'o' and the value that return is 12
print(myString.index('y'))
print(myString[5])
print(myString[-3])
print(myString[2])

myName= "Charles"
myNumber = 23
myDoubleNumer= 24.6
print("My name is "+ myName)
#Other form for concatenate
print("........................................")
print(f"My name is {myName}")
print(f"My number is {myNumber}")
print(f"My double number is {myDoubleNumer}")
#Another form for concatenate
print("........................................")
print("My name is {0}".format(myName))
print("My number is {0}".format(myNumber))
print("My double number is {0}".format(myDoubleNumer))

