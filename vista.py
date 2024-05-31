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
        existe = self.userController.log_in(usuario, password)
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


# class VentanaMenu(QDialog):
#     def __init__(self,ppal=None):
#         super().__init__(ppal)
#         loadUi("ventana_menu.ui",self)
#         self.__ventanaPadre=ppal
#         self.setup()

#     def setup(self):
#         self.ingresar_pac.clicked.connect(self.abrir_ventana_ingresar)
#         self.eliminar_pac.clicked.connect(self.abrir_ventana_eliminar)
#         self.salida.clicked.connect(self.abrir_ventana_principal)
    
#     def abrir_ventana_ingresar(self):
#         ventana_ingresar= VentanaIngreso(self)
#         self.hide()
#         ventana_ingresar.show()
    
#     def abrir_ventana_eliminar(self):
#         ventana_eliminar= VentanaEliminar(self)
#         self.hide()
#         ventana_eliminar.show()
    
#     def abrir_ventana_principal(self):
#         ventana_principal= VentanaMenu(self)
#         self.hide()
#         ventana_buscar.show()

#     def setControlador(self,c):
#         self.__miCoordinador = c

# app=QApplication(sys.argv)
# mi_vista=ventanaLogin()
# mi_vista.show()
# sys.exit(app.exec())