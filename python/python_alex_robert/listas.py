"""
Las listas son un tipo de datos abstracto (modelo teorico que define un conjunto de datos
y las operaciones que se pueden realizar sobre ellos.)
"""
#Metodos de una lista
#append: agrega un elemento a la lista
frutas = ["manzanas", "bananas", "naranjas"]
frutas.append("ciruelas")
print(frutas)
for fruta in frutas:
    print(fruta)

#insert: inserta un elemento en una posicion especifica
frutas.insert(1,"kiwi")
print(frutas)

#extend: permite añadir una lista a la lista inicial
otras_frutas = ["mandarinas", "uvas", "sandias"]
frutas.extend(otras_frutas)
print(frutas)

#remove: elimina la primer ocurrencia del elemento especificado
frutas.remove("manzanas")
print(frutas)

#index: devuelve el indice de la primera ocurrencia del elemento especificado
posicion = frutas.index("bananas")
print(f"Las bananas estan en la posicion {posicion}")