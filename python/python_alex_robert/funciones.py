def calcular_precio_con_iva(valor_sin_iva, iva=21):
    resultado = valor_sin_iva * (1 + (iva / 100))
    return resultado

print(calcular_precio_con_iva(5000))