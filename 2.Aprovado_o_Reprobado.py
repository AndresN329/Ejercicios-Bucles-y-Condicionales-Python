#Aprovado o reprobado

print("-" * 40)

while True:
    try:
       Nota = float(input("\nPor favor, indica tu nota al programa: "))

       if 0 <= Nota < 60:
        print("\nJaja pendejo reprobaste")
        break
       elif 60 <= Nota <= 100:
        print("\nFelicitaciones aprobaste")
        break
       else:
        print("\nSolo numero de 0 A 100")
    except ValueError:
        print("\nEse no es un dato valido, solo numero de 0 a 100 >:()")
    