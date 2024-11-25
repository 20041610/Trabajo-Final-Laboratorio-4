"""
Problema:
Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar
(se ingresa un valor entero en el precio del producto)
"""
precioDelProducto= int(input("Ingrese el precio del producto: "))
cantidadDelProducto = int(input("Que cantidad va a llevar? : "))
importe = precioDelProducto * cantidadDelProducto
print("El importe es: $",importe)