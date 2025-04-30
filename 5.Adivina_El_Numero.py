#Adivina el numero

print("-" * 40)
print("       Adivina es Numero ")
print("-" * 40)

import random

numero_ramdom = random.randint(1,10)
Intentos = 3

while Intentos > 0:
    try:

       NumeroU = int(input(f"\nIntenta adivinar el numero entre 1 y 10, tienes {Intentos} intentos: "))

       if NumeroU > numero_ramdom:
           print("\nEl numero es menor :0")
       elif NumeroU < numero_ramdom:
           print("\nEl numero es mayor")
       else:
           print("\nAdivinaste el numero :0")
           break
       
       Intentos -= 1

    except ValueError:
        print("\nPro favor ingresa un numero -_-")

if NumeroU == numero_ramdom:
    print("\nEl numero era",numero_ramdom)
else:
    print("\nJAJAJA pendejo no adivinste, el numero era ", numero_ramdom)
    

