import sqlite3
from datetime import datetime
import re

class Academia:
    def abrir_conexion(self):   
        try:
            variable_de_conexion = sqlite3.connect('test.db')
            print("Conexión abierta")
            cursor = variable_de_conexion.cursor()

            # Habilitar claves foráneas
            cursor.execute("PRAGMA foreign_keys = ON")

            # Crear tabla de estudiantes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tabla_estudiantes (
                    id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_estudiante VARCHAR(50) NOT NULL,
                    fecha_nacimiento DATE NOT NULL,
                    dni VARCHAR(20) NOT NULL
                )
            ''')

            # Crear tabla de materias
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tabla_materias (
                    id_materia INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_materia VARCHAR(50) NOT NULL
                )
            ''')

            # Crear tabla intermedia para la relación muchos a muchos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS estudiantes_materias (
                    id_relacion INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_estudiante INTEGER NOT NULL,
                    id_materia INTEGER NOT NULL,
                    FOREIGN KEY (id_estudiante) REFERENCES tabla_estudiantes (id_estudiante),
                    FOREIGN KEY (id_materia) REFERENCES tabla_materias (id_materia)
                    UNIQUE (id_estudiante, id_materia)
                )
            ''')

            print("Tablas creadas con éxito \n")
            return variable_de_conexion

        except sqlite3.Error as e:
            print(f"Error al abrir la conexión: {e}")
            return None

    
    def validar_nombre(self,nombre_str):
                    if (not nombre_str):
                        print("Error. El nombre no puede estar vacio")
                        return False
                    elif (not re.match(r"^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s]+$", nombre_str)):
                        print("Error.Contiene caracteres invalidos")                        
                        return False
                    elif ("  " in nombre_str):
                        print("Error. No pueden haber espacios consecutivos")
                        return False
                    elif (len(nombre_str) < 2 or len(nombre_str) > 50):
                        print("Error. Nombre demasiado largo")
                        return False
                    else:
                        print("Correcto")
                        print(nombre_str.strip().title())
                        print(len(nombre_str))
                        input("ENTER para continuar")
                        return nombre_str.strip().title()
                    
                    


    def validar_fecha(self,fecha_str):
        try:
            fecha = datetime.strptime(fecha_str, '%d-%m-%Y')
            if (fecha > datetime.now()):
                print("La fecha no puede ser en el futuro.")
                return False 
            edad = ((datetime.now() - fecha).days // 365)
            if (edad < 18 or edad > 100):
                print(f"La edad ({edad} años) no es válida.")
                return False
            print("Fecha válida.")
            return fecha.strftime("%Y-%m-%d")
        except ValueError:
            print("El formato de fecha no es válido. Use DD-MM-YYYY.")
            return False

    def validar_dni(self , dni_str: str) ->str | bool:
        if (not dni_str):
            print("Error. No puede estar vacio.")
            return False
        if(not dni_str.isdigit()):
            print("Error. Caracteres invalidos. Solo numeros")
            return False
        if (len(dni_str) != 8):
            print("Error. El dni debe tener 8 digitos.")
            return False
        print("DNI correcto.")
        return dni_str


    def insertar_datos(self,nombre,fecha_nacimiento,dni):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO tabla_estudiantes(nombre_estudiante, fecha_nacimiento, dni) VALUES(?,?,?)",(nombre,fecha_nacimiento,dni))
        conexion.commit()
        conexion.close()
        print("Datos ingresados correctamente")

    def lectura_datos(self):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_estudiantes")
        datos = cursor.fetchall()
        conexion.close()
        return datos

    def lectura_especifica(self, id):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_estudiantes WHERE id_estudiante = (?)", (id,))
        datos = cursor.fetchone()
        conexion.close()
        return datos

    
    def borrar_datos(self, id_a_borrar):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM tabla_estudiantes WHERE id_estudiante = (?)",(id_a_borrar,))
        if(cursor.rowcount == 0):
            print("Error. No hay estudiante con ese id.")
            conexion.close()
            return False
        else:
            print(self.lectura_especifica(id_a_borrar))
            continuar = input("Confirmar borrado ? s/n: ").lower()
            if(continuar != "s"):
                conexion.close()
            else:
                print("Ha sido eliminado")
                conexion.commit()
                conexion.close()
                return True
    def modificar_datos(self, id_a_modificar,nuevo_nombre,nueva_fecha, nuevo_dni):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("UPDATE tabla_estudiantes SET nombre_estudiante = (?), fecha_nacimiento = (?), dni = (?) WHERE id_estudiante = (?)", (nuevo_nombre,nueva_fecha,nuevo_dni,id_a_modificar))
        conexion.commit()
        conexion.close()
    
    def ver_materias(self):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_materias")
        datos = cursor.fetchall()
        conexion.close()
        return datos
    
    def ver_materia_especifica(self,id_materia):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tabla_materias WHERE id_materia = (?)",(id_materia,))
        datos = cursor.fetchone()
        conexion.close()
        return datos

    
    def insertar_estudiantes_en_materias(self, id_estudiante, id_materia):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        registro = self.ver_materia_y_estudiante_especifico(id_estudiante,id_materia)
        if(registro):
            print("El estudiante ya esta inscripto en esa materia")
        else:
            cursor.execute("INSERT INTO estudiantes_materias(id_estudiante,id_materia) VALUES (?,?)",(id_estudiante,id_materia))
            conexion.commit()
            print("Estudiante inscrito correctamente en la materia.")
        conexion.close()



    def ver_materias_con_estudiantes(self):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute('''
        SELECT 
            em.id_relacion, 
            e.nombre_estudiante, 
            e.dni, 
            m.nombre_materia 
        FROM estudiantes_materias em
        INNER JOIN tabla_estudiantes e ON em.id_estudiante = e.id_estudiante
        INNER JOIN tabla_materias m ON em.id_materia = m.id_materia
    ''')        
        datos = cursor.fetchall()
        conexion.close()
        return datos
    
    def ver_materia_y_estudiante_especifico(self, id_estudiante, id_materia):
        conexion = self.abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM estudiantes_materias WHERE id_estudiante = (?) AND id_materia = (?)",(id_estudiante, id_materia))
        datos = cursor.fetchone()
        conexion.close()
        return datos
        


"""
/*import mysql.connector*/

/*id: Identificador único de cada paciente (clave primaria).
nombre: Nombre del paciente.
apellido: Apellido del paciente.
edad: Edad del paciente.
direccion: Dirección del paciente.
telefono: Teléfono de contacto.
obra_social: Obra social del paciente.
descuento: Porcentaje de descuento en atención (si aplica). */

import sqlite3

def conectar():
    conexion = sqlite3.connect('centro_medico.db')
    return conexion

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            descuento REAL
            edad INTEGER,
            direccion TEXT,
            telefono TEXT,
            obra_social TEXT,

        )
    ''')
    conexion.commit()
    conexion.close()

# Ejecutamos la función para crear la tabla si no existe
crear_tabla()



def listar_pacientes():
 conexion = conectar()
 cursor = conexion.cursor()
 cursor.execute('SELECT * FROM Pacientes')
 pacientes = cursor.fetchall()
 conexion.close()
 for paciente in pacientes:
        print(paciente)
"""
"""
def agregar_paciente(nombre, apellido, edad, direccion, telefono, obra_social, descuento): 
    conexion = conectar() 
    cursor = conexion.cursor() 
    cursor.execute(''' INSERT INTO Pacientes (nombre, apellido, edad, direccion, telefono, obra_social, descuento) VALUES (?, ?, ?, ?, ?, ?, ?) ''', (nombre, apellido, edad, direccion, telefono, obra_social, descuento)) 
    conexion.commit()
    #verificacion de carga con una busqueda e impresion de datos
    conexion.close() 
    print("Paciente agregado correctamente.")
    
deg Actualiza_Paciente

if nombre:
    campos.append('nombre = ?')
    valores.append(nombre)
if apellido:
    campos.append('apellido = ?')
    valores.append(apellido)
if edad:
    campos.append('edad = ?')
    valores.append(edad)
if direccion:
    campos.append('direccion = ?')
    valores.append(direccion)
if telefono:
    campos.append('telefono = ?')
    valores.append(telefono)
if obra_social:
    campos.append('obra_social = ?')
    valores.append(obra_social)
if descuento is not None:
    campos.append('descuento = ?')
    valores.append(descuento)

query += ', '.join(campos)
query += ' WHERE id = ?'
valores.append(id)

cursor.execute('''
INSERT INTO Pacientes (nombre, apellido, edad, direccion, telefono, obra_social, descuento)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (nombre, apellido, edad, direccion, telefono, obra_social, descuento))

cursor.execute(query, valores)
conexion.commit()
conexion.close()
print("Paciente actualizado correctamente.")


**Eliminar un paciente**:


```python
def eliminar_paciente(id):
 conexion = conectar()
 cursor = conexion.cursor()
 cursor.execute('DELETE FROM Pacientes WHERE id = ?', (id,))
 conexion.commit()
 conexion.close()
 print("Paciente eliminado correctamente.")
 
 def actualizar_paciente(id, nombre=None, apellido=None, edad=None, direccion=None, telefono=None, obra_social=None, descuento=None): conexion = conectar() cursor = conexion.cursor() # Construimos la consulta dinámica para actualizar solo los campos proporcionados query = 'UPDATE Pacientes SET ' campos = [] valores = []

Copiar código
if nombre:
    campos.append('nombre = ?')
    valores.append(nombre)
if apellido:
    campos.append('apellido = ?')
    valores.append(apellido)
if edad:
    campos.append('edad = ?')
    valores.append(edad)
if direccion:
    campos.append('direccion = ?')
    valores.append(direccion)
if telefono:
    campos.append('telefono = ?')
    valores.append(telefono)
if obra_social:
    campos.append('obra_social = ?')
    valores.append(obra_social)
if descuento is not None:
    campos.append('descuento = ?')
    valores.append(descuento)

query += ', '.join(campos)
query += ' WHERE id = ?'
valores.append(id)

cursor.execute(query, valores)
conexion.commit()
conexion.close()
print("Paciente actualizado correctamente.")
css
Copiar código

4. **Eliminar un paciente**:

```python
def eliminar_paciente(id):
 conexion = conectar()
 cursor = conexion.cursor()
 cursor.execute('DELETE FROM Pacientes WHERE id = ?', (id,))
 conexion.commit()
 conexion.close()
 print("Paciente eliminado correctamente.")
 
 
 
"""