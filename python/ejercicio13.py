"""
Confeccionar un programa que permita cargar un número 
entero positivo de hasta tres cifras y muestre un 
mensaje indicando si tiene 1, 2, o 3 cifras. 
Mostrar un mensaje de error si el número de cifras es mayor.

"""
num = int(input("Ingrese un numero entero positivo de hasta 3 cifras:"))
while(num < 0):
    num = int(input("No puede ser negativo.Ingrese nuevamente hasta 3 cifras:"))

if(num >=0 and num<=9):
        print("El numero tiene una cifra. Es", num)
else:
        if(num >=10 and num <=99):
            print("El numero tiene dos cifras. Es",num)
        else:
            if(num >=100 and num <=999):
                print("El numero tiene tres cifras. Es", num)
            else:
                print("Error. Tiene mas de tres cifras. Chau pa.")

"""
Lo que hice fue ingresar un numero entero, y mediante un
while validar que si es negativo me obligue a ingresar
nuevamente un numero. Luego mediante condicionales 
anidados validé si el numero contiene 1,2 o 3 cifras, o
si tiene mas de tres enviar un mensaje de error.
"""