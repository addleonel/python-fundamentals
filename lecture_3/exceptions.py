# MORE INFORMATION
# https://docs.python.org/3/tutorial/errors.html

# class B(Exception):
#   pass

# class C(B):
#   pass

# class D(C):
#   pass

# for cl in [B, C, D]:
#   try:
#     raise cl
#   except D:
#     print("D")
#   except B:
#     print("B")
#   except C:
#     print("C")

# try:
#   raise NameError
#   raise SyntaxError
# except Exception:
#   print("hello there is a error") 
  




# for k in [NameError, ValueError, SyntaxError]:
#   try:
#     raise k
#   except NameError:
#     print("There is a NameError")
#   except ValueError:
#     print("There is a ValueError")
#   except SyntaxError:
#     print("There is a SyntaxError")


# try:
#     with open("myfile.txt", "r") as f:
#       lines = f.readlines()
#       for l in lines:
#         print(l.strip('\n'))
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# USING try ... except ... else ... finally
for k in [1.0,"two", 3.0]:
    try:
        i = int(k)
    except ValueError:
        print("Error")
    else:
        print("yep")
    finally:
        print("completed process\n"+"="*30)



"""
Si hay una finallycláusula presente, la finally cláusula se ejecutará como la última tarea 
antes de try que se complete la instrucción. La finallycláusula se ejecuta 
independientemente de si la trydeclaración produce o no una excepción. Los siguientes 
puntos discuten casos más complejos cuando ocurre una excepción:

1- Si se produce una excepción durante la ejecución de la try cláusula, 
  la excepción puede ser manejada por una except cláusula. 
  Si la except cláusula no maneja la excepción, 
  la excepción se vuelve a generar después de que la finally cláusula se haya ejecutado.

2- Una excepción podría ocurrir durante la ejecución de una except o elsecláusula. 
  Nuevamente, la excepción se vuelve a generar después de finallyque se haya ejecutado la cláusula.

3- Si la trydeclaración llega a una break, continueo returncomunicado, 
  la finallycláusula se ejecutará justo antes del break, continueo return la ejecución de declaración.

4- Si una finallycláusula incluye una return declaración, el valor devuelto será el de 
  la declaración de la finallycláusula return, no el valor de la declaración de la trycláusula return.
"""
1-
# try:
#   raise NameError("Hi error")
# except SyntaxError:
#   print("error SyntaxError")
# finally:
#   print("FINISHED")
3-
# n = 0
# while n < 10:
#   try:
#     print(n)
#     if n == 4:
#       break
#     print("Bye")
#   except Exception:
#     print("Error")
#   finally:
#     print("finished")
#   n += 1
4- 
# def example():
#   try:
#     return True
#   finally:
#     return False
# print(example()) # return False

# CORRECT USE of try ... except ... else ... finally ...

def divide(x, y):
    try:
        r = x/y
    except ZeroDivisionError:
        print("Not divide by zero")
    except TypeError:
        print("Not input an string")
    else:
        print("the result is: {}".format(round(r, 2)))
    finally:
        print("completed process\n" + "="*30)

divide(2, 3)
divide(2, 0)
divide('2', '3')
divide(10, 2)





