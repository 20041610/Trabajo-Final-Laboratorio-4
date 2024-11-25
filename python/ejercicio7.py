"""
Calcular el sueldo mensual de un operario conociendo 
la cantidad de horas trabajadas y el valor por hora.
"""
horasTrabajadas = int(input("Cuantas horas trabajó? : "))
while(horasTrabajadas < 8 ):
 horasTrabajadas = int(input("No puede ser menor a 8 horas. Ingrese nuevamente:  "))
    
precioPorHora = int(input("Cuanto cobra por hora? : "))
sueldoPorDia = horasTrabajadas * precioPorHora
sueldoPorMes = sueldoPorDia * 24
print("El sueldo por mes del operario es: ", sueldoPorMes)
