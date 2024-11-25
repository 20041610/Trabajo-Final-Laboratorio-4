"""
Las matrices son estructuras de datos bidimensionales (de dos dimensiones)
con elementos agrupados en filas y columnas.
"""
#Declarar una matriz: Puede estar compuesta por tipos de datos o tipos de estructuras y mas
matriz = [[1,2,3,4],
          [5,6,7,8]]#Las listas son las filas y los elementos formasn las columnas
print(matriz)

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        print(matriz[fila][columna],end=" ")
    print(",")

cadena = "A contar"
for letra in range(len(cadena)):
    print(cadena[letra])