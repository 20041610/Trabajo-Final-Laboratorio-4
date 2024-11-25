"""
Ingresar tres numeros, y si alguno es menor a 10, imprimir
un mensaje que diga "almenos un numero es menor a 10"
"""


def obtenerTresNumeros():
    """Esta funcion pretende ingresar tres numeros y almacenarlos en un array. Contempla excepciones y devuelve
    con return la lista cargada. Esto permite usar la lista cargada en cualquier lugar del codigo"""
    numeros = []
    for i in range(3):
        while True:
            try:
                num = int(input(f"Ingrese el numero {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Error. Ingrese numeros enteros")
    return numeros

def imprimirNumeros(referencia_a_lista_numeros): 
    """Imprime los numeros usando un for que dice que cada "elemento" en la lista "referencia_a_lista_numeros" 
    se imprima"""

    print("\nLos numeros ingresados son:")
    for elemento in referencia_a_lista_numeros:
        print(elemento)

def obtenerMenorADiez(referencia_a_lista_numeros):
    contador= sum(1 for elemento in referencia_a_lista_numeros if elemento <10)#Con sum, se suma
    #los numeros que se le pasan como parametro. En este caso se suman numeros 1 ya que hay una condicion que indica que
    #se genere un 1 por cada iteracion del for que devuelva un elemento mmenor a 10
    if(contador == 3):
        print("Todos los numeros son menores a diez")

listaDeNumeros = obtenerTresNumeros()#Hay que almacenar si o si en una variable lo que devuelve la funcion para poder usarlo en las demas funciones
imprimirNumeros(listaDeNumeros)
obtenerMenorADiez(listaDeNumeros)


