"""
Se ingresan tres notas de un alumno, si el promedio es 
mayor 
o igual a siete mostrar un mensaje "Promocionado".
"""
nota1 = int(input("Ingrese la primer nota: "))
while(nota1 >10 or nota1 < 1  ):
    nota1 = int(input("No puede tener ese valor. Ingrese nuevamente: "))

nota2 = int(input("Ingrese la segunda nota: "))
while(nota2 >10 or nota2 < 1  ):
    nota2 = int(input("No puede tener ese valor. Ingrese nuevamente: "))

nota3=int(input("Ingrese la tercer nota: "))
while(nota3 >10 or nota3 < 1  ):
    nota3 = int(input("No puede tener ese valor. Ingrese nuevamente: "))

promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 7:
    print("Promocionado/a con",promedio)
else:
    print("No promocionado/a con",promedio)