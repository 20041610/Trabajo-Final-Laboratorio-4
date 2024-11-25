import mysql.connector



class ConexionCompleta:
    def __init__ (self):
        self.conexion =mysql.connector.connect(host="localhost", user="root" ,password="jcrc24PA", database="bd1python")
    
    def __init_subclass__(self,nombre,profesion):
        self.nombre = nombre
        self.profesion = profesion

    def __str__(self) -> str:

        datos= self.consulta_ciudades()
        aux=""
        for row in datos:
            aux = aux + str(row) + "\n"
            return aux
    
    
    def Insertar (self, nombre,profesion):
        cursor = self.conexion.cursor()
        cursor.execute( "INSERT INTO usuarios(nombre,profesion)VALUES('{}','{}')".format(nombre,profesion))
        cursor.close()
        self.conexion.commit()

    def consulta(self):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        datos= cursor.fetchall()
        cursor.close()
        for row in datos:
            print(f"Id: {row[0]}, Nombre:{row[1]}, Profesión:{row[2]}")

    def ConsultaEspecifica(self, id_usuario):
        cursor = self.conexion.cursor()
        sql = '''SELECT * FROM usuarios WHERE id_usuario = {}'''.format(id_usuario)
        cursor.execute(sql)
        datoEspecifico = cursor.fetchone()
        cursor.close()
        return datoEspecifico
    

    def Eliminar(self, id_usuario):
        self.id_usuario = id_usuario
        cursor = self.conexion.cursor()
        sql='''DELETE FROM usuarios WHERE id_usuario= {}'''.format(id_usuario)
        cursor.execute(sql)
        cursor.close()
        self.conexion.commit()
    
    def Modificar(self,id_usuario,nombre,profesion):
        
        cursor = self.conexion.cursor()
        sql = '''UPDATE usuarios SET nombre = '{}', profesion ='{}' WHERE id_usuario = {}'''.format(nombre,profesion,id_usuario)
        cursor.execute(sql)
        self.conexion.commit()
        cursor.close()
    

    
    