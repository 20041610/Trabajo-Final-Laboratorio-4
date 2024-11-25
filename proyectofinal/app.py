from flask import Flask#Importar flask
from flask import render_template #Importa una herramienta que nos lleva al archivo que le pasemos, como index.html
from flask import request #Recepciona la informacion que ingresamos en los form

from flask import redirect #Sirve para direccionarnos y mostrarnos la informacion que buscamos
from flask import session #Importa las variables de sesion
from flask_mysqldb import MySQL #Importa herramientas para poder usar Mysql
from datetime import datetime#Importa funciones de tipo fecha y tiempo
from flask import send_from_directory#Es para encontrar archivos que esten en el directorio
import os

app = Flask(__name__,)
app.secret_key = "perdon"
mysql=MySQL()#conexion
#variables de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='jcrc24PA'
app.config['MYSQL_DB']='bd_libros'
mysql.init_app(app)



@app.route('/')#Cuando acceda o cuando le soliciten informacion
def inicio():#va a devolver un index
    return render_template('sitio/index.html')

@app.route('/imagenes/<imagen>')
def imagenes(imagen):
    return send_from_directory(os.path.join('templates/sitio/imagenes'),imagen  )

@app.route('/css/<archivocss>')
def css_link(archivocss):
    return send_from_directory(os.path.join('templates/sitio/css/'),archivocss)

@app.route('/js/<archivojs>')
def js_link(archivojs):
    return send_from_directory(os.path.join('templates/sitio/js/'),archivojs)

"""@app.route('/<settingsjs>')
def settingsJs(settingsjs):
    return send_from_directory(os.path.join('/settings.js'),settingsjs )
"""
@app.route('/settings')
def settingsJs():
    return render_template('settings.js')
@app.route('/nosotros')
def nosotros():#va a llevarnos al archivo nosotros.html
    return render_template('sitio/nosotros.html')

@app.route('/libros')#Nos lleva a la seccion libros.html
def libros():#va a llevarnos al archivo nosotros.html
    
    cursor3 = mysql.connection.cursor()
    cursor3.execute("SELECT * FROM tabla_libros")
    datosDeLibros = cursor3.fetchall()
    return render_template('sitio/libros.html' , libros = datosDeLibros)

@app.route('/admin/login')
def admin_login():
    return render_template('admin/login.html')

@app.route('/admin/login', methods = ['POST'])
def admin_login_post():
    _usuario = request.form['usuario']
    _contraseña = request.form['contraseña']
    if _usuario == "admin" and _contraseña == "1234":
        session["login"] = True
        session["usuario"] = "Pa'"
        return redirect("/admin")
    return render_template('admin/login.html', mensaje="Acceso Denegado")

@app.route('/admin/cerrar')
def admin_login_cerrar():
    session.clear()
    return redirect('/admin/login')


@app.route('/admin/')

def admin_index():
    if( not 'login' in session):
        return redirect('/admin/login')
    return render_template('admin/index.html')

#acceder a libros del lado del admin
@app.route('/admin/libros')#Nos lleva a la seccion libros.html de admin
def admin_libros():#va a llevarnos al archivo libros.html de la seccion admin
    
    if( not 'login' in session):
        return redirect('/admin/login')
    sql = "SELECT * FROM tabla_libros"
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    datosDeLibros = cursor.fetchall()
    return render_template('admin/libros.html', libros = datosDeLibros)



@app.route('/admin/libros/guardar', methods=['POST'])#En esta instruccion se recibe la URL del formulario del que queremos recepcionar datos
def admin_libros_guardar():
    _nombre = request.form['nombreDelLibro']
    _imagen = request.files['imagenDelLibro']
    _url = request.form['urlDelLibro']
    
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%Y%H%M%S')
    if (_imagen.filename != ""):
        nuevoNombre = horaActual + "_" + _imagen.filename
        _imagen.save("templates/sitio/imagenes/"+nuevoNombre)



    dml = ("INSERT INTO tabla_libros (nombre_libro,imagen_libro,url_libro) VALUES ('{}','{}','{}')").format(_nombre,nuevoNombre,_url)
    cursor = mysql.connection.cursor()
    cursor.execute(dml)
    mysql.connection.commit()
    
    print(request.form['nombreDelLibro'])#request para recepcionar los datos y form para especificar qué form
    return redirect('/admin/libros')#nos redirecciona

@app.route('/admin/libros/borrar', methods=['POST'])
def admin_libros_borrar():
    _id = request.form['txtID']

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT imagen_libro FROM tabla_libros WHERE id_libro = %s",(_id,))
    datosDeLibros = cursor.fetchall()

    if os.path.exists("templates/sitio/imagenes/"+str(datosDeLibros[0][0])):
        os.unlink("templates/sitio/imagenes/"+str(datosDeLibros[0][0]))
    
    cursor.execute("DELETE FROM tabla_libros WHERE id_libro = %s",(_id,))
    mysql.connection.commit()

    return redirect('/admin/libros')

@app.route('/admin/actualizar', methods=['POST'])
def admin_actualizar():
    _id = request.form['txtID']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tabla_libros WHERE id_libro = %s ",(_id,))
    booksData = cursor.fetchall()
    return render_template('admin/actualizar.html', booksData = booksData)

@app.route('/admin/libros/actualizar', methods=['POST'])
def admin_libros_actualizar():
    _id = request.form['txtID']
    _nuevoNombre = request.form['nuevoNombreDelLibro']
    _nuevaUrl = request.form['nuevaUrlDelLibro']
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE tabla_libros SET nombre_libro = %s, url_libro = %s WHERE id_libro = %s ",(_nuevoNombre,_nuevaUrl,_id))
    mysql.connection.commit()
    _nuevaImagen = request.files['nuevaImagenDelLibro']
    tiempo = datetime.now()
    horaActual = tiempo.strftime('%Y%H%M%S')
    if (_nuevaImagen.filename != ""):
        cursor.execute("SELECT imagen_libro FROM tabla_libros WHERE id_libro = %s",(_id,))
        datosDeLibros = cursor.fetchall()
        if os.path.exists("templates/sitio/imagenes/"+str(datosDeLibros[0][0])):
            os.unlink("templates/sitio/imagenes/"+str(datosDeLibros[0][0]))
        nuevoNombreImagen = horaActual + "_" + _nuevaImagen.filename
        _nuevaImagen.save("templates/sitio/imagenes/"+nuevoNombreImagen)
        cursor.execute("UPDATE tabla_libros SET imagen_libro = %s WHERE id_libro = %s",(nuevoNombreImagen, _id))
        mysql.connection.commit()
    return redirect('/admin/libros')#nos redirecciona

"""@app.route('/carrito', methods=['POST'])
def carrito():
    _id = request.form['txtID']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tabla_libros WHERE id_libro = %s",(_id,))
    datosDeLibros = cursor.fetchall()
    return render_template("sitio/carrito.html", datosDeLibros = datosDeLibros)
"""
@app.route('/carrito/agregar/', methods=['POST'])
def agregar():
    libro_id = request.form['txtID']
    _cantidadesAComprar = int(request.form['cantidadesAComprar'])
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tabla_libros WHERE id_libro = %s", (libro_id,))
    producto = cursor.fetchone()
    if producto:
        if 'carrito' not in session:
            session['carrito'] = []
        # Asegúrate de que los datos del producto se almacenen como un diccionario
        nuevo_producto = {'id': producto[0], 'nombre': producto[1], 'imagen': producto[2], 'precioUnitario': producto[4], 'cantidad': _cantidadesAComprar, 'importe': (_cantidadesAComprar * producto[4])  }
        # Verifica que el producto no esté ya en el carrito, si quieres permitir duplicados, omite esta parte
        #if nuevo_producto not in session['carrito']:
        session['carrito'].append(nuevo_producto)

        # Actualiza la sesión
        session.modified = True

    return redirect('/libros')

@app.route('/carrito')
def carrito():
    carrito = session.get('carrito', [])
    #total = sum([p['precio'] for p in carrito])
    return render_template('sitio/carrito.html',carrito=carrito ) 
""", total=total"""

@app.route('/loginusuario')
def login_usuario():
    return render_template('sitio/loginusuario.html')


@app.route('/usuario/login', methods = ['POST'])
def usuario_login_post():
    _usuario = request.form['usuario']
    _contraseña = request.form['contraseña']

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT count(*) as usuario_encontrado FROM tabla_clientes WHERE nombre_cliente = %s and contraseña_cliente = %s ",(_usuario,_contraseña))
    _usuario_encontrado = cursor.fetchone()
    
    for registro in _usuario_encontrado:
        if  (registro >0):
            session["loginusuario"] = _usuario
            return redirect ('/')
    return render_template('sitio/loginusuario.html', mensaje="Acceso Denegado")


if __name__ == '__main__':#Si la aplicacion esta lista
    app.run(debug=True)#Corremos el index y los cambios que hagamos tambien se van a mostrar
