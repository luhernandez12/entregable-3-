from pymongo import MongoClient

class login:
    def __init__(self):
        self.__usuario=""
        self.__contraseña=""
    
    def verUsuario(self):
        return self.__usuario
    def verContraseña(self):
        return self.__contraseña
    def agregarUsuario(self,usuario):
        self.__usuario=usuario
    def agregarContraseña(self,contraseña):
        self.__contraseña=contraseña
    
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

class Conexion:
    def __init__(self,uri,nombre_db):
        self.cliente = MongoClient(uri)
        self.db= self.cliente[nombre_db]
        return True
    

class Sistema:

    def login(self,uri,nombre_db):
        conexion=Conexion(uri,nombre_db)
    def ingresarPaciente(nombre_coleccion,n,a,e,i):
        p=Paciente()       
        documento:{"nombre":p.asignarNombre(n),"apellido":p.asignarApellido(a),"Edad":p.asignarEdad(e),"ID":p.asignarId(i)}
        coleccion=Conexion.db[nombre_coleccion]
        coleccion.insert_one(documento)


s=Sistema()
f=Sistema.login('mongodb://localhost:27017', 'base datos ')
if f==True:
    Sistema.ingresarPaciente('pacientes','juan','jimenez',30,1235)
