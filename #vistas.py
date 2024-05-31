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

    def recibir_info(self,n,r,f,c,e):
            self.__miCoordinador.recibir_info(n,r,f,c,e)

class VentanaMenu(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("ventana_menu.ui",self)
        self.__ventanaPadre=ppal
        self.setup()

    def setup(self):
        self.ingresar_pac.clicked.connect(self.abrir_ventana_ingresar)
        self.eliminar_pac.clicked.connect(self.abrir_ventana_eliminar)
        self.buscar_pac.clicked.connect(self.abrir_ventana_buscar)
        self.salida.clicked.connect(self.abrir_ventana_principal)
    
    def abrir_ventana_ingresar(self):
        ventana_ingresar= VentanaIngreso(self)
        self.hide()
        ventana_ingresar.show()
    
    def abrir_ventana_eliminar(self):
        ventana_eliminar= VentanaEliminar(self)
        self.hide()
        ventana_eliminar.show()
    
    def abrir_ventana_buscar(self):
        ventana_buscar= VentanaBuscar(self)
        self.hide()
        ventana_buscar.show()
    
    def abrir_ventana_principal(self):
        ventana_principal= VentanaMenu(self)
        self.hide()
        ventana_buscar.show()

    def setControlador(self,c):
        self.__miCoordinador = c

class VentanaAgregar():
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("ventana_agregar.ui",self)
        self.__ventanaPadre=ppal
        self.setup()

class VentanaEliminar():
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("ventana_eliminar.ui",self)
        self.__ventanaPadre=ppal
        self.setup()

class VentanaBuscar():
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("ventana_agregar.ui",self)
        self.__ventanaPadre=ppal
        self.setup()
        
    
        



app=QApplication(sys.argv)
vista=VentanaMenu()
vista.show()
sys.exit(app.exec_())
