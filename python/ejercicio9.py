"""
Realizar un programa que solicite la carga por teclado
de dos números, si el primero es mayor al segundo
informar su suma y diferencia, en caso contrario 
informar el producto y la división del primero respecto 
al segundo.

"""
num1 = int(input("Ingrese el primer numero:"))
num2 = int(input("Ingrese el segundo numero: "))
if num1 > num2 :
    suma = num1 + num2
    resta = num1 - num2
    print("La suma de los numeros da: ", suma)
    print("La resta de los numeros da: ", resta)

else:
    multiplicacion = num1 * num2
    division = num1 / num2
    print("La multiplicacion de ambos numeros da:",multiplicacion)
    print("La division de ambos numeros da:", division)