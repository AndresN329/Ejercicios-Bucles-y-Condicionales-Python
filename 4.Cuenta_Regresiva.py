#Contador hasta 0 (o cuenta regresiva)

print("-" * 40)
print("       Cuenta Regresiva :0")
print("-" * 40)

while True:
    try:
        Numero = int(input("\nIngresa un número positivo para la cuenta regresiva: "))

        if Numero >= 0:
         print("\nEmpieza la cuenta regresiva...")
         while Numero >= 0:
            print(Numero)
            Numero -= 1 
         print("Magia :0")
         break
        else:
         print("\nPor favor, ingresa un número positivo")
    except ValueError:
        print("\nDato incorrecto ingresa solo números")
