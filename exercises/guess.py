

def adivina(number_adivina):
    while True:
        numero = int(input("Ingresa el numero: "))
        if numero > number_adivina:
            print("Muy alto")
        elif numero < number_adivina:
            print("Muy bajo")
        else:
            print("Lo conseguirte!")
            break


if __name__ == '__main__':
    adivina(23)