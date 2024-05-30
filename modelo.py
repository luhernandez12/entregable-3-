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



