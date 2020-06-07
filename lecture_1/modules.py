 
#using functions

def printLine():
    print("")

def creditConsole():
    option=0
    principalSald=0
    name =""
    surname=""
    password=""
    while option !=5:
        print("----WELCOME TO SIMPLE SYSTEM-----")
        print("we need your colaboration:")
        print("")
        print("1. input your mont. ")
        print("2. output part of your sald.")
        print("3. View your data and actual sald")
        print("4. If your don't have a account sign in now HERE")
        print("5. exit")
        print("")
    
        option = int(input("Option: "))
        
        if option == 1:
            printLine()
            print("Welcome to this section:")
            printLine()
            principalSald = principalSald + optionOne(principalSald)
        elif option ==2:
            printLine()
            principalSald=principalSald-optionTwo(principalSald)
        elif option ==3:
            printLine()
            optionThree(name,surname,password)
            print("your actual sald is: ", principalSald)
            printLine()
        elif option ==4:
            printLine()
            if principalSald>0:
                print("you already have an account")
                condition = input("Do you want to change your datas? (s/n): ")
                if condition == "s":
                    name = optionFourName()
                    surname = optionFourSurname()
                    password = optionFourPassword()
                elif condition =="n":
                    print()
                else:
                    while condition != "s" and condition != "n":
                        print("Try again")
                        condition = input("Do you want to change your datas? (s/n): ")
                        if condition == "s":
                            name = optionFourName()
                            surname = optionFourSurname()
                            password = optionFourPassword()     
                        elif condition =="n":
                            print()
            else:
                name = optionFourName()
                surname = optionFourSurname()
                password = optionFourPassword()
                principalSald = principalSald + optionFour()
        elif option >5 or option <1:
            printLine()
            print("This values is not in the option. Try again")
            printLine()
        else:
            printLine()
            optionFive()
            printLine()
    

# option 1
def optionOne(principalCount):
    sumCount=0
    if principalCount==0:
        print("you don't have a account in this system, please create one in the fourth section")
        print("thank for this")
        printLine()
    else:
        sumCount =  float(input("Insert your sald: "))
        printLine()
        if sumCount<0:
            while sumCount<0:
                print("this value is not allow, try again")
                sumCount =  float(input("Insert your sald: "))
            printLine()
            print("Thank for this")
            printLine()
    return sumCount              
# option 2
def optionTwo(principalCount):
    restCount=0
    if principalCount==0:
        print("you don't have a account in this system, please create one in the fourth section")
        print("thank for this")
        printLine()
    else:
        restCount =  float(input("Insert your sald: "))
        printLine()
        if restCount<0:
            while restCount<0:
                print("this value is not allow, try again")
                restCount =  float(input("Insert your sald: "))
            printLine()
            print("Thank for this")
            printLine()
    return restCount 
# option 3
def optionThree(name, surname, password):
    if name =="" and surname =="" and password =="":
        print("You don't have an acount. Do it in the fourth section")
    else:
        print("Your name is: ",name)
        print("Your surname is: ", surname)
        condition = input("Do you want to view your password? (s/n): ")
        if condition == "s":
            print("your password is: ",password)
        elif condition =="n":
            print()
        else:
            while condition != "s" and condition != "n":
                print("Try again")
                condition = input("Do you want to view your password? (s/n): ") 
                if condition == "s":
                        print("your password is: ",password)
                elif condition =="n":
                    print() 
                
# option 4 
def optionFour():
    prinpicalCount = float(input("Insert you inicial mont: "))
    print("")
    print("thanks for this")
    return prinpicalCount
def optionFourName():
    name = input("Insert your name: ")
    return name
def optionFourSurname():
    username= input("Insert your username: ")
    return username
def optionFourPassword():
    password = input("Insert your password: ")
    return password
# def optionFourChange(name,surname,password):
    


# option 5
def optionFive():
    print("Thanks for watching")

# run
creditConsole()

