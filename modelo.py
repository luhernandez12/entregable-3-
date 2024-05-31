import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPoint, Qt, QByteArray, QIODevice, QBuffer
import sqlite3
from PyQt5.QtCore import QObject
import json 

class Paciente:
    def __init__(self):
        self.__nombre=""
        self.__apellido=""
        self.__edad=int
        self.__id=int
    
    def verNombre(self):
        return self.__nombre
    def verApellido(self):
        return self.__apellido
    def verEdad(self):
        return self.__edad
    def verId(self):
        return self.__id
    def asignarNombre(self, n):
        self.__nombre=n
    def asignarApellido(self,a):
        self.__apellido=a
    def asignarEdad(self,e):
        self.__edad=e
    def asignarId(self,i):
        self.__id=i

class LoginModelo():
    def __init__(self,user="usuarios.json"):
        self.user=user
        self.load()
    
    def load(self):
        try:
            with open (self.user,'r') as file:
                self.usuario=json.load(file)
        except FileExistsError:
            self.users=[]
            print("No hay usuarios ")
    
    def existe(self, usuario,password ):
       for i in self.usuario:
            if i["usuario"]==usuario and i["password"]==password:
                return 1    
            else:
                return 2


class Sistema:
    def __init__(self, nombre_db="almacenamiento.db"):  # Se establece como atributos el nombre de la base de datos, la conexión con la base y el cursor 
        self.nombre_db = nombre_db
        self.conexion = sqlite3.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()
        # Crear la tabla Paciente si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Paciente (
            id INTEGER PRIMARY KEY,
            nombre TEXT, 
            apellido TEXT,  
            edad INTEGER
            )''')
        self.conexion.commit()
        self.cursor.close()
       

    def asignar_paciente(self,n, a, i, e):  # Se establecen estos parámetros que vendrán ligados con el controlador y la vista 
        p = Paciente()  # Se crea objeto paciente para luego usar los métodos de asignación de atributos 
        p.asignarNombre(n)
        p.asignarApellido(a)
        p.asignarId(i)
        p.asignarEdad(e)
        self.cursor = self.conexion.cursor()
        if not self.conexion:  # Verificar inicialmente si se conectó correctamente a la base de datos 
            print("No hay conexión a la base de datos")
            return 
        query_check = "SELECT * FROM Paciente WHERE id = ?"  # Se identifica el parámetro por el cual se va a buscar el paciente 
        self.cursor.execute(query_check, (p.verId(),))  # Se usa el método ver_cedula de la clase paciente para verificar si el paciente que se quiere ingresar aún no está en la base de datos
        if self.cursor.fetchone() is None:  # Si no se encuentra entonces se usa condicional para agregar paciente 
            query_insert = '''                
            INSERT INTO Paciente ( nombre, apellido, id, edad)
            VALUES ( ?, ?, ?, ?)
            '''  # Se hace la identificación de parámetros en la tabla de la base de datos Paciente 
            parametros = (p.verNombre(),p.verApellido(), p.verId(),p.verEdad())
            self.cursor.execute(query_insert, parametros)  # Se relaciona el query_insert con la tupla de parámetros del paciente
            self.conexion.commit()
            self.cursor.close()
            return True 
            print(f"Paciente con la cédula {p.verId()} agregado a la base de datos")  # Retorno de mensaje para verificar en consola la ejecución del código 
        else:
                print(f"Paciente con la cédula {p.verId()} ya existe en la base de datos")
                self.cursor.close()
        
    def buscar_eliminar(self, nombre):
    
        self.cursor = self.conexion.cursor()
        if not self.conexion:  # Verificar inicialmente si se conectó correctamente a la base de datos 
            print("No hay conexión a la base de datos")
            return 
        query_search = "SELECT * FROM Paciente WHERE LOWER(nombre) LIKE ?"
        self.cursor.execute(query_search, (f'{nombre.lower()}%',))
        resultados = self.cursor.fetchall()
        lista_pacientes = []
        for paciente in resultados:
            paciente_dict = {
                "id": paciente[0],
                "nombre": paciente[1],
                "apellido": paciente[2],
                "edad": paciente[3]
            }
            lista_pacientes.append(paciente_dict)
        return lista_pacientes 
    
    def eliminar_paciente(self, cedula):
            if not self.conexion:   
                print("No hay conexión a la base de datos")
                return 

            try:
                self.cursor = self.conexion.cursor()
                query_delete = "DELETE FROM Paciente WHERE id = ?"
                self.cursor.execute(query_delete, (cedula,))
                self.conexion.commit()
                self.cursor.close()
                print(f"Paciente con cédula {cedula} eliminado exitosamente.")
                return True
            except sqlite3.Error as e:
                print(f"Error al eliminar el paciente: {e}")
                self.conexion.rollback()
            finally:
                if self.cursor:
                    self.cursor.close()

# l=LoginModelo()
# d=l.existe("user1",123)
# if d==1:
#     s=Sistema("almacenamiento.db") 
#     s.asignar_paciente("tania","quin",16,19)
#     i=s.buscar_eliminar("Lu")
#     print(i)
#     o=int(input("Ingresar id de paciente a eliminar"))
#     s.eliminar_paciente(o)





