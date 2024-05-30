import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPoint, Qt, QByteArray, QIODevice, QBuffer
import sqlite3
from PyQt5.QtCore import QObject
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import pandas as pd

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
   
class Sistema:
    def __init__(self, nombre_db):  # Se establece como atributos el nombre de la base de datos, la conexión con la base y el cursor 
        self.nombre_db = nombre_db
        self.conexion = sqlite3.connect(self.nombre_db)
        self.cursor = self.conexion.cursor()
        self.login={}
        
        

        # Crear la tabla Paciente si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Paciente (
            id INTEGER PRIMARY KEY,
            nombre TEXT, 
            apellido TEXT,  
            edad INTEGER
            )''')
        self.conexion.commit()
        self.cursor.close()
    
    def entrada(self, usuario, clave):  #login 
        # Aquí estamos usando un diccionario para login con un ejemplo
        self.login["user13"] = 123

        # Verificar si la llave existe en el diccionario
        if usuario in self.login:
            # Verificar si la clave coincide con el valor asociado a la llave
            if self.login[usuario] == clave:
                print("Las credenciales son correctas.")
                return True
            else:
                print("La clave es incorrecta.")
                return False
        else:
            print("La llave no existe en el diccionario.")
            return False
    
    def asignar_paciente(self,n, a, i, e):  # Se establecen estos parámetros que vendrán ligados con el controlador y la vista 
        self.cursor = self.conexion.cursor()
        if not self.conexion:  # Verificar inicialmente si se conectó correctamente a la base de datos 
            print("No hay conexión a la base de datos")
            return 
        p = Paciente()  # Se crea objeto paciente para luego usar los métodos de asignación de atributos 
        p.asignarNombre(n)
        p.asignarApellido(a)
        p.asignarId(i)
        p.asignarEdad(e)
        
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
            print(f"Paciente con la cédula {p.verId()} agregado a la base de datos")  # Retorno de mensaje para verificar en consola la ejecución del código 
        else:
            print(f"Paciente con la cédula {p.verId()} ya existe en la base de datos")
            self.cursor.close()

p = Sistema('almacenamiento.db')
usuario = input("Ingrese la llave (nombre de usuario): ")
contraseña = int(input("Ingrese la clave (contraseña): "))

# Llamar al método de instancia login
if p.entrada(usuario, contraseña):
    p.asignar_paciente("luisa", "quintero", 199, 20)



