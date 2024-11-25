from ejerciciosqlite import Academia

objeto_academia = Academia()

menu = '''
****************************
*        Menu Carrera      *
****************************
*                           *
* 1) Insertar Estudiantes      *
* 2) Eliminar Estudiantes      *
* 3) Modificar Estudiantes     *
* 4) Ver los datos de cada estudiante*
* 5) Ver lista de materias*
* 6) Insertar estudiante en materia*
* 7) Ver materias y sus estudiantes*
* 8) Salir*
****************************

'''

def main():
    opcion = 0
    while(not opcion == 8):
        print(menu)
        while True:
            try:
                opcion= int(input("Ingrese una opcion del menu:"))
                break
            except ValueError:
                print("Ingrese numeros")
        if(opcion==1):
            print("Insertar personas")
            nombre = input("Ingrese el nombre: ")
            while(True):
                nombre_ingresado = objeto_academia.validar_nombre(nombre)
                if(nombre_ingresado == False):
                    nombre = input("Ingrese el nombre nuevamente: ")
                else:
                    continuar = input(f"El nombre ingresado fué {nombre}. Aceptar? s/n: ").lower()
                    if(continuar !="s"):
                        nombre = input("Ingrese el nombre nuevamente: ")
                    else:
                        break

            fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato DD-MM-YYYY: ")
            while True:
                fecha_ingresada = objeto_academia.validar_fecha(fecha_nacimiento)
                if(fecha_ingresada == False):
                    fecha_nacimiento = input("Ingrese la fecha de nacimiento nuevamente (DD-MM-YYYY): ")
                else:
                    break

            dni = input("Ingrese su DNI (Solo numeros): ")
            while True:
                dni_ingresado = objeto_academia.validar_dni(dni)
                if(dni_ingresado == False):
                    dni = input("Ingrese su dni nuevamente (Solo numeros): ")
                else:
                    break
            objeto_academia.insertar_datos(nombre_ingresado,fecha_ingresada,dni_ingresado)



        if(opcion == 2):
            continuar = "s"
            while(continuar == "s"):
                registros = objeto_academia.lectura_datos()
                if(not registros):
                    print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
                    input("ENTER para continuar")
                    break
                else:
                        id_a_borrar = input("Ingrese el id de el/la estudiante a eliminar: ")
                        while True:
                            id_encontrado = objeto_academia.borrar_datos(id_a_borrar)
                            if(id_encontrado == False):
                                reintentar = input("Desea intentar nuevamente? s/n: ")
                                if(reintentar != "s"):
                                    print("Operacion cancelada")
                                    break
                                id_a_borrar = input("Ingrese nuevamente el id de el/la estudiante a eliminar: ")
                            else:
                                break
                        continuar = input("Desea continuar eliminando estudiantes? s/n: ").lower()
        if(opcion == 3):
            print("Modificar estudiante")
            continuar = "s"
            while (continuar == "s"):
                registros = objeto_academia.lectura_datos()
                if(not registros):
                    print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
                    input("ENTER para continuar.")
                    break
                else:
                    while True:
                        try:
                            id_a_modificar = int(input("Ingrese el id de el/la estudiante a modificar: "))
                            break
                        except ValueError:
                            print("Error. Debe ingresar un numero entero.")
                    estudiante_encontrado = objeto_academia.lectura_especifica(id_a_modificar)
                    if( not estudiante_encontrado):
                        print("Error. No hay ningun estudiante con ese id")
                        input("Ingrese ENTER para continuar")
                    else:
                        print(f"La persona con ese id es: {estudiante_encontrado}") 
                        modificar = input("Modificar nombre? s/n: ").lower()
                        if(modificar != "s"):
                            nombre_ingresado = estudiante_encontrado[1]
                        else:
                            nombre = input("Ingrese el nombre: ")
                            while(True):
                                nombre_ingresado = objeto_academia.validar_nombre(nombre)
                                if(nombre_ingresado == False):
                                    nombre = input("Ingrese el nombre nuevamente: ")
                                else:
                                    continuar = input(f"El nombre ingresado fué {nombre}. Aceptar? s/n: ").lower()
                                    if(continuar !="s"):
                                        nombre = input("Ingrese el nombre nuevamente: ")
                                    else:
                                        break

                        modificar = input("Modificar fecha de nacimiento? s/n: ").lower()
                        if(modificar != "s"):
                            fecha_ingresada = estudiante_encontrado[2]
                        else:
                            fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato DD-MM-YYYY: ")
                            while True:
                                fecha_ingresada = objeto_academia.validar_fecha(fecha_nacimiento)
                                if(fecha_ingresada == False):
                                    fecha_nacimiento = input("Ingrese la fecha de nacimiento nuevamente (DD-MM-YYYY): ")
                                else:
                                    break
                        modificar = input("Modificar dni? s/n: ")
                        if(modificar != "s"):
                            dni_ingresado = estudiante_encontrado[3]
                        else:
                            dni = input("Ingrese su DNI (Solo numeros): ")
                            while True:
                                dni_ingresado = objeto_academia.validar_dni(dni)
                                if(dni_ingresado == False):
                                    dni = input("Ingrese su dni nuevamente (Solo numeros): ")
                                else:
                                    break
                        objeto_academia.modificar_datos(id_a_modificar,nombre_ingresado,fecha_ingresada,dni_ingresado)

                        
                    continuar = input("Seguir buscando y modificando? s/n: ").lower()

        if (opcion == 4):
            print("Tabla de alumnos/as")
            registros = objeto_academia.lectura_datos()
            for registro in registros:
                print(f"ID del/la estudiante: {registro[0]}")
                print(f"Nombre del/la estudiante: {registro[1]}")
                print(f"Fecha de nacimiento del/la estudiante: {registro[2]}")
                print(f"DNI del/la estudiante: {registro[3]}")
                print("-" * 40)  # Separador entre registros
            input("ENTER para continuar")
        
        if(opcion ==5):
            print("Lista de materias")
            registros = objeto_academia.ver_materias()
            for registro in registros:
                print(f"ID de la materia: {registro[0]}||Nombre de la materia: {registro[1]}")
                print("-" * 40)  # Separador entre registros

            input("ENTER para continuar")
        
        if(opcion==6):
            print("Insertar estudiante en materia")
            continuar = "s"
            while(continuar == "s"):
                registros = objeto_academia.lectura_datos()
                if(not registros):
                    print("No hay datos en la base de datos. Use la opcion 1 para insertar datos.")
                    input("ENTER para continuar")
                    break
                else:
                    for registro in registros:
                        print(f"ID de el/la estudiante: {registro[0]}||Nombre de el/la estudiante: {registro[1]}")
                    
                    try:
                            id_estudiante = int(input("Ingrese el id de el/la estudiante"))
                            estudiante_encontrado = objeto_academia.lectura_especifica(id_estudiante)
                            if (not estudiante_encontrado):
                                print("No hay estudiante con ese id")
                                input("ENTER para continuar")
                                break
                            else:
                                try:
                                    id_materia = int(input("Ingrese el id de la materia: "))
                                    materia_encontrada = objeto_academia.ver_materia_especifica(id_materia)
                                    if(not materia_encontrada):
                                        print("No hay materia con ese id.")
                                        input("ENTER para continuar")
                                        break
                                
                                except ValueError:
                                    print("Error.Inserte un numero entero como id.")

                                
                    except ValueError:
                            print("Debe ingresar un numero entero")

                    objeto_academia.insertar_estudiantes_en_materias(id_estudiante,id_materia)
                    continuar = input("Seguir insertando alumnos a materias? s/n: ").lower()

        if(opcion ==7):
            print("Materias y sus alumnos")
            registros = objeto_academia.ver_materias_con_estudiantes()
            for registro in registros:
                print(f"Id de la relacion: {registro[0]} || Estudiante: {registro[1]} || DNI: {registro[2]} || Materia: {registro[3]}")
                print("-" * 40)
            input("ENTER para continuar")
                    

                

            
            

main()