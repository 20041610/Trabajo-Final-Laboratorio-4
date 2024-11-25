"""
Un postulante a un empleo, realiza un test de 
capacitación, se obtuvo la siguiente información: 
cantidad total de preguntas que se le realizaron y la 
cantidad de preguntas que contestó correctamente. 
Se pide confeccionar un programa que ingrese los dos 
datos por teclado e informe el nivel del mismo según 
el porcentaje de respuestas correctas que ha obtenido, 
y sabiendo que:
Nivel maximo: porcentaje >=90%
Nivel medio: porcentaje >=75% y <90%
Nivel regular: >=50% y <75%
Fuera de nivel: <50%

"""

while True:
    entrada =(input("Ingrese la cantidad de preguntas a responder:"))#Ingreso un valor 
    if(entrada.isdigit()):#Si es numero, lo voy a guardar en una nueva variabe
        cantidadDePreguntas = int(entrada)
        print("Ingresó el",cantidadDePreguntas)
        if(cantidadDePreguntas ==0):#Si el numero es 0, no salgo del bucle y sigo ingresando
            print("No pueden haber 0 preguntas CABEZAAA")
        else:#si no, salgo 
            break
    else:
        print("Error. Ingrese numeros")#Si en "entrada" no ingrese un numero, sigo en el bucle  

while True:
    entrada2 = input("Ingrese la cantidad de preguntas correctas:")
    if(not entrada2.isdigit()):#Si entrada2 no es numero no se guarda en cantidadCorrectas hasta que sea un numero
        print("Deben ser numeros")
    else:
        cantidadDeCorrectas = int(entrada2)
        print("Ingresó el",cantidadDeCorrectas)
        if(cantidadDeCorrectas>cantidadDePreguntas):#Si cantidadCorrectas es mayor que cantidadDePreguntas
            print("NOOOO ASI NOOO")
        else:
            break

porcentajeCorrectas = (cantidadDeCorrectas / cantidadDePreguntas)*100#Obtengo el porcentaje de preguntas correctas
print("El porcentaje de correctas es de ", porcentajeCorrectas,"%")
if(porcentajeCorrectas<50 ):#Segun el porcentaje, declaro el nivel
            print("Fuera de nivel.", porcentajeCorrectas)
elif(porcentajeCorrectas >=50 and porcentajeCorrectas < 75):
            print("Nivel regular.", porcentajeCorrectas)
elif(porcentajeCorrectas >=75 and porcentajeCorrectas <90):
            print("Nivel medio.", porcentajeCorrectas)
elif(porcentajeCorrectas >=90):
            print("Nivel alto.", porcentajeCorrectas)
"""
def obtener_cantidad_preguntas():
    while True:
        entrada = input("Ingrese la cantidad de preguntas a responder: ")
        if entrada.isdigit():
            cantidad_de_preguntas = int(entrada)
            if cantidad_de_preguntas == 0:
                print("No pueden haber 0 preguntas.")
            else:
                return cantidad_de_preguntas
        else:
            print("Error. Ingrese números.")

def obtener_cantidad_correctas(cantidad_de_preguntas):
    while True:
        entrada2 = input("Ingrese la cantidad de preguntas correctas: ")
        if entrada2.isdigit():
            cantidad_de_correctas = int(entrada2)
            if cantidad_de_correctas > cantidad_de_preguntas:
                print("La cantidad de correctas no puede ser mayor que la cantidad de preguntas.")
            else:
                return cantidad_de_correctas
        else:
            print("Deben ser números.")

def calcular_porcentaje_correctas(cantidad_de_correctas, cantidad_de_preguntas):
    return (cantidad_de_correctas / cantidad_de_preguntas) * 100

def determinar_nivel(porcentaje_correctas):
    if porcentaje_correctas < 50:
        return "Fuera de nivel."
    elif porcentaje_correctas < 75:
        return "Nivel regular."
    elif porcentaje_correctas < 90:
        return "Nivel medio."
    else:
        return "Nivel alto."

def main():
    cantidad_de_preguntas = obtener_cantidad_preguntas()
    cantidad_de_correctas = obtener_cantidad_correctas(cantidad_de_preguntas)
    porcentaje_correctas = calcular_porcentaje_correctas(cantidad_de_correctas, cantidad_de_preguntas)
    print(f"El porcentaje de correctas es de {porcentaje_correctas:.2f}%")
    nivel = determinar_nivel(porcentaje_correctas)
    print(nivel)

if __name__ == "__main__":
    main()

"""