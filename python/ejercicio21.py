"""
Ingresar una fecha cualquiera y verificar si es navidad
"""
while True:
    entrada = input("Ingrese un mes cualquiera:")

    if(entrada == 'enero' or entrada == "febrero" or entrada == "marzo" or entrada == "abril" or entrada == "mayo" or entrada == "junio" or entrada == "julio" or entrada == "agosto" or entrada == "septiembre" or entrada == "octubre" or entrada == "noviembre" or entrada == "diciembre"):
        print("Mes correcto")
        print(f'El mes ingresado es {entrada}')
        break
    else:
        print("No es un mes")

while True:
    entrada2 = input("ingrese una fecha de ese mes:")
    if(not entrada2 .isdigit()):
        print("Deben ser numeros")
    elif(entrada2 .isdigit()):
        dia = int(entrada2)
        if(((entrada == "enero" or entrada == "marzo" or entrada == "mayo" or entrada == "julio" or entrada == "agosto" or entrada == "octubre" or entrada == "diciembre") and (dia <=0 or dia >31)) 
        or (entrada =="febrero" and(dia <=0 or dia>28))
        or ((entrada =="abril" or entrada == "junio" or entrada == "septiembre" or entrada == "noviembre") and(dia <=0 or dia > 30))):
            print(f"Error. {entrada} no puede tener {dia} dias")
        else:
            print(f"La fecha es {entrada} {dia}")
            break
if(entrada == "diciembre" and dia == 25):
    print("La felicida a a a a ")
        



