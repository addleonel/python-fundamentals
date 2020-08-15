import math
class methods:

  def filter_method(self):
    try :
      listnumber = []
      inter = int(input("type the number times: "))
      for k in range(inter):
        inter = int(input("type any integer numbers: "))
        listnumber.append(inter)
      print("your number: ", listnumber)
      # using annonymous method 
      def prime2(n):
        lst = []
        for i in range(2, n):
          if n%i != 0:
            lst.append(True)
          else:
            lst.append(False)
        return lst
      def isprime(number):
        return all(prime2(number))
      
      listfiltered = filter(isprime, listnumber)
      listprime = list(listfiltered)
      print("In your list there is {} prime numbers".format(len(listprime)))
      print(listprime)
      print("-"*50)
    except:
      print("this is not a integer number, try again")
myobject = methods()
myobject.filter_method()

# c
def prime(n):
  return all(n%i for i in range(2, n))


    