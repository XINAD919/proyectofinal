from flask import Flask,render_template,request,redirect,url_for
from flask.helpers import flash
from flask_mysqldb import MySQL
#metodo principal
app = Flask(__name__)
#MySQL Conexion
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='proyectoxdb'
mysql = MySQL(app)

#sesion
app.secret_key='My secret key'# protege la sesion la guarda en las cookies

#rutas
@app.route('/')
def home():
  return render_template('index.html') 

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/registrar')
def registro():
  return render_template('registro.html')

#metodo para registrar usuario-----------------------------------------------------------------------
@app.route('/registrarUsuario', methods = ['POST'])
def registrarse():
  if request.method == 'POST':
    nombre = request.form['nombre']
    correo= request.form['correo']
    contraseña= request.form['contraseña'] 
    cur=mysql.connection.cursor()
    cur.execute('INSERT INTO usuarios(Nombre,Correo,Contraseña)VALUES(%s,%s,SHA2(%s, 512))',
                (nombre, correo, contraseña)) ## aqui se declara la sentencia SQL pero no se ejecuta
    flash('el usuario fue creado exitosamente','success')
    mysql.connection.commit() ### este ejecuta la sentencia SQL
    return redirect(url_for('registro'))
  #-------------------------------------------------------------------
#metodo para iniciar sesion--------------------------------------------------------------------------
@app.route('/iniciarSesion', methods = ['POST'])
def iniciarSesion():
  if request.method == 'POST':
    correo= request.form['correo']
    contraseña= request.form['contraseña']
    cur=mysql.connection.cursor()
    
    cur.execute('SELECT Nombre, Correo FROM usuarios WHERE correo = %s AND contraseña = SHA2(%s, 512)',
                (correo, contraseña))
        
    rs = cur.fetchone() #guarda lo que nos devuelve la ejecucion de la sentencia sql
    
    if rs == None:
      flash('Algo no coincide con tu información','error')
      return redirect(url_for('login'))
    else:
      flash('Bienvenido'+ ' '+ rs[0], 'success')
      return redirect(url_for('home'))
#--------------freeconk-----------------------------------------------------------
@app.route('/Vistos-recientemente')
def vistoReciente():
  pass
@app.route('/Informacion-General')
def generalInfo():
  pass
@app.route('/payment-methods')
def paymethods():
  pass
@app.route('/Ayuda y atención al cliente')
def atencionCliente():
  pass

if __name__ == "__main__":
   app.run(debug= True)