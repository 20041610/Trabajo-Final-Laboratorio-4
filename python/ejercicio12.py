"""
Se cargan por teclado tres números 
distintos. Mostrar por pantalla el mayor de ellos
"""

num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero:"))
while(num2 == num1):
    num2 = int(input("Ya ingresaste ese numero. Ingresa otro:"))

num3 = int(input("Ingrese el tercer numero:"))
while(num3 == num1 or num3 == num2):
    num3 = int(input("Ya ingresaste ese numero. Ingresa otro:"))


if(num1>num2 and num1 > num3 ):
    print("El primer numero es el mayor. Es", num1)
else:
    if(num2 > num3):
        print("El segundo numero es el mayor. Es", num2)
    else:
        print("El tercer numero es el mayor. Es", num3)