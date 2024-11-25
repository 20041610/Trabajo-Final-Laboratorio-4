"""
Ingresar el sueldo de una persona, si supera los 
3000 dolares mostrar un mensaje 
en pantalla indicando que debe abonar impuestos
"""
sueldo = int(input("Ingrese el sueldo de una persona: "))
if sueldo >3000 :
    print("Esta persona debe abonar impuestos.")
else:
    print("Esta persona no debe abonar impuestos.")