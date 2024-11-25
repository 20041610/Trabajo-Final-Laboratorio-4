def calcular_factorial(numero):
    if(numero == 0):
        resultado = 1
    else:
        resultado = numero * calcular_factorial(numero-1)
    return resultado

print(calcular_factorial(5))

"""
● La gestión de memoria en las funciones recursivas se
realiza mediante la pila de llamadas.
● Cada vez que se llama a una función recursiva, se agrega
una nueva instancia de esa función a la pila de llamadas.
● A medida que la función se llama recursivamente se
acumulan mas y mas instancias en la pila.
● Cuando se alcanza la condición de salida, las funciones
comienzan a desapilarse, en caso de que dicha condición
no se cumpla y se llegue a cierto límite (llamado el límite de
recursión), python lanzará un error de desbordamiento de
pila (RecursionError).
"""