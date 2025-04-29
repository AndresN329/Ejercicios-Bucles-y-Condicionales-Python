#Clasificador de nuemeros

print("-" * 40)
print("       Clasificador de numeros")
print("-" * 40)

while True : 
    try: 
        Numero = int(input("\nPor favor, ingresa un numero entero: "))

        if Numero > 0:
            print("\nTu numero es positivo :0")
        elif Numero < 0:
            print("\nTu numero es negativo :0")
        else:
            print("\nTu numero es 0")
    except ValueError:
        print("\nDato incorrecto, por favor ingrese un numero entero >:c")