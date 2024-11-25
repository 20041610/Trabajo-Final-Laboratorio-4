"""
Se ingresa por teclado un número 
positivo de uno o dos dígitos (1..99) mostrar un 
mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para 
tener dos dígitos un número entero)

"""
num1 = int(input("Ingrese un numero positivo: "))
while(num1 < 0):
    num1 = int(input("Error. Ingrese un numero positivo:"))

if(num1 >= 0 and num1 <= 9):
    print("El numero tiene un solo digito. Es",num1)
elif (num1 >9 and num1<=99):
    print("El numero tiene dos cifras. Es",num1)

else:
    print("El numero tiene mas de dos cifras")

    