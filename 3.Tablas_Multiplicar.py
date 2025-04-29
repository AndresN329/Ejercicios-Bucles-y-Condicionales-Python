#Tablas de multiplicar 

print("-" * 40)
print("        Tablas de Multiplicacion")
print("-" * 40)

while True:
    try:
        Numeros = int(input("\nIngresa el numero de la tabal que quieres saber: "))
        print("\nOk, esta es la tabla del", Numeros)

        for numero in range(1,11):
            Tablas = Numeros * numero
            print(Numeros,"x",numero,"=",Tablas)
    except ValueError:
        print("\nIngrese un numero por favor")



#Estaba intentando que solo aceptara numeros positivos pero aun no pude :)
"""
print("-" * 40)
print("        Tablas de Multiplicacion")
print("-" * 40)

while True:
    try:
        Numeros = int(input("\nIngresa el numero de la tabal que quieres saber: "))

        for numero in range(1,11):
            Tablas = Numeros * numero
            if Numeros > 0:
              print("\nOk, esta es la tabla del", Numeros)
              print(Numeros,"x",numero,"=",Tablas)
              print("\nGracias por usar el programa :)")
            else:
                print("\nPor favor que sea un numero positivo")
                break
    except ValueError:
        print("\nIngrese un numero por favor")
"""