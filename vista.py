#vistas

import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox,QLineEdit,QTextEdit
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
from controlador import* 


class ventanaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ventana_ingreso.ui",self)
        self.userControler=login_controlador()
        self.usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.password.setValidator(QIntValidator())
        self.setup()

    def setup(self):
        
        self.boton_ingresar.clicked.connect(self.validardatos)
        self.boton_salir.clicked.connect(self.closeOption)

    def validardatos(self):
        username = self.usuario.text()
        password = self.password.text()
        existe = self.userController.log_in(username, password)
        if isinstance(existe, tuple):
            self.vetView = VentanaMenu()
            self.vetView.show()
            self.close()
        elif existe == 0:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("No existe un usuario con los \ndatos proporcionados")
            msgBox.setWindowTitle('Datos incorrectos')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()

    def closeOption(self):
        self.close()


class VentanaMenu(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("ventana_menu.ui",self)
        self.vetController = sistema_controlador()
        self.setup()

    def setup(self):
        self.menu_agregar.clicked.connect(self.abrir_ventana_ingresar)
        self.menu_eliminar.clicked.connect(self.abrir_ventana_eliminar)
        self.menu_salir.clicked.connect(self.abrir_ventana_logout)
        self.boton_agregar.clicked.connect(self.agregar_paciente)
        self.boton_buscar.clicked.connect(self.tabla)
    

    def abrir_ventana_ingresar(self):
        ventana_ingresar=self.stackedWidget.setCurrentIndex(1)
    def abrir_ventana_eliminar(self):
        ventana_eliminar= self.stackedWidget.setCurrentIndex(2) 
    def abrir_ventana_logout(self):
        self.ventanaL=ventanaLogin()
        self.ventanaL.show()
        self.close()
    
    def agregar_paciente(self):
        iden = self.id.text()
        nombre = self.nombre.text()
        edad = self.edad.text()
        apellido = self.apellido.text()
        if not iden or not nombre or not apellido or not edad:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Debe ingresar todos los datos")
            msgBox.setWindowTitle('Datos faltantes')
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.exec()
        else:
            isUnique = self.vetController.asignar_paciente(nombre,apellido,edad,iden)
            if not isUnique:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("La id ya existe")
                msgBox.setWindowTitle('Id repetida')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.information)
                msgBox.setText("La id ya existe")
   
    def tabla(self):
        nombre=self.buscar_paciente.text()
        lista_datos=self.vetController.buscar_paciente(nombre)
        self.tabla_eliminar.setColumnCount(len(lista_datos[0]))
        headers = list(lista_datos[0].keys())
        self.tabla_eliminar.setHorizontalHeaderLabels(headers)

        for i, fila in enumerate(lista_datos):
            for j, valor in enumerate(fila.values()):
                item =self.tabla_eliminar(str(valor))
                self.tabla_eliminar.setItem(i, j, item)
    

    

       
    
    

app=QApplication(sys.argv)

mi_vista2=VentanaMenu()
mi_vista2.show()


sys.exit(app.exec())