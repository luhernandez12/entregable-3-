#vistas

import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox,QLineEdit,QTextEdit
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi


class ventanaPrincipal(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("ventana_ingreso.ui",self)
        self.setup()

    def setup(self):
        self.usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.password.setValidator(QIntValidator())
        self.boton_ingresar.clicked.connect(self.validardatos)
        self.boton_salir.clicked.connect(self.closeOption)

    def setCoordinador(self,c):
        self.__coordinador = c

    def validardatos(self):
        pass
        username = self.usuario.text()
        password = self.password.text()
        verificar = self.__coordinador.validarusuario(username,password)
        if verificar:
            
            self.hide()
            self.newWindow = Vista()
            self.newWindow.setCoordinador(self.__coordinador)
            self.newWindow.show()
    
        else:
            QMessageBox.warning(self, "Error de inicio de sesión", "Usuario o contraseña incorrectos.")
    def closeOption(self):
        self.close()



app=QApplication(sys.argv)
vista=ventanaPrincipal()
vista.show()
sys.exit(app.exec_())
