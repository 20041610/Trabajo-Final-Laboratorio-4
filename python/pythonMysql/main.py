import time
from conexion import ConexionCompleta


personas = ConexionCompleta()

menu = '''******************
*        Menu Personas      *
****************************
*                           *
* 1) Insertar Personas      *
* 2) Eliminar Personas      *
* 3) Modificar Personas     *
* 4) Imprimir tabla         *
* 5) Salir                  *
****************************

'''

def main():

    opcion = 0
    while(not opcion ==5):
        print(menu)
        while True:
            try:
                opcion= int(input("Ingrese una opcion del menu:"))
                break
            except ValueError:
                print("Ingrese numeros")

        

        if (opcion == 1):
            print("Insertar Personas")
            nombre = input("Ingrese el nombre de la persona: ")
            profesion = input("Ingrese su profesion: ")
            if(nombre and profesion):
                personas.Insertar(nombre,profesion)
                print("Persona insertada con exito")
                time.sleep(1)
        elif(opcion == 2):
            print("Eliminar personas")
            id_usuario=int(input("Ingrese el id de la persona a eliminar: "))
            if(id_usuario):
                personas.Eliminar(id_usuario)
                print("Persona eliminada.")
                time.sleep(2)

        elif(opcion ==3):
            print("Modificar personas")
            while True:
                try:
                    id_usuario=int(input("Ingrese el id de la persona a modificar: "))
                    break
                except ValueError:
                    print("Ingrese numeros")
            ConsultaEspecifica = personas.ConsultaEspecifica(id_usuario)

            if(ConsultaEspecifica == 0):
                print("Error. No hay ningun usuario con ese id")
                input("Ingrese ENTER para continuar")
            else:
                print(f"La persona con ese id es: {personas.ConsultaEspecifica(id_usuario)}")
                
                nombre = input("Ingrese un nuevo nombre para esa persona: ")
                profesion = input("Ingrese la nueva profesion: ")
                if(nombre ==''):
                    nombre = ConsultaEspecifica[1]
                if(profesion==''):
                    profesion = ConsultaEspecifica[2]   
                personas.Modificar(id_usuario,nombre,profesion)
                print(f"Nuevos datos de la persona: {personas.ConsultaEspecifica(id_usuario)}")
                input("Ingrese ENTER para continuar")

        
        
        elif(opcion ==4):
            print("Mostrar Personas")
            print(personas.consulta())
            input("Enter para continuar")
        elif(opcion == 5):
            print("Saliendo...")
        else:
            print("Opcion no valida")
            input("Enter para continuar")

main()