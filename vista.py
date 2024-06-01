
import sys 
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QLineEdit, QPushButton, QTableWidgetItem
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
from controlador import* 


class ventanaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ventana_ingreso.ui",self)
        self.userControler=login_controlador()
        # self.usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        # self.password.setValidator(QIntValidator())
        self.setup()

    def setup(self):
        
        self.boton_ingresar.clicked.connect(self.validardatos)
        self.boton_salir.clicked.connect(self.closeOption)

    def validardatos(self):
        username = self.usuario.text()
        password = self.password.text()
        existe = self.userControler.log_in(username, password)
        if isinstance(existe, tuple):
            self.vetView = VentanaMenu()
            self.vetView.show()
            
            
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
        self.boton_eliminar.clicked.connect(self.eliminar_pac)
        self.boton_menu.clicked.connect(self.abrir_ventana_menu)
        self.tabla()
    
    def abrir_ventana_menu(self):
        ventana_menu=self.stackedWidget.setCurrentIndex(0)   

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
            self.abrir_ventana_menu()
            
            if not isUnique:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("La id ya existe")
                msgBox.setWindowTitle('Id repetida')
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.exec()
            # else:
            #     msgBox = QMessageBox()
            #     msgBox.setIcon(QMessageBox.information)
            #     msgBox.setText("La id ya existe")
    
        
    def tabla(self):
        buscar_n=self.buscar_paciente.text()
        if buscar_n!=None:
            self.listaPacientes = self.vetController.buscar_paciente(buscar_n)
            self.tabla_eliminar.setRowCount(len(self.listaPacientes)) 
            self.tabla_eliminar.setColumnCount(4) 
            columnas = ["ID", "Nombre", "Apellido", "Edad"]
            columnLayout = ['id','nombre','apellido','edad']
            self.tabla_eliminar.setHorizontalHeaderLabels(columnas)
            for row, pacientes in enumerate(self.listaPacientes):
                for column in range(4):
                    item = QTableWidgetItem(pacientes[columnLayout[column]])
                    self.tabla_eliminar.setItem(row, column, item)
            
                    
            self.tabla_eliminar.setColumnWidth(0, 80)  
            self.tabla_eliminar.setColumnWidth(1, 110)  
            self.tabla_eliminar.setColumnWidth(2, 60)  
            self.tabla_eliminar.setColumnWidth(3, 60)  
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.information)
            msgBox.setText("No existen personas con este nombre ")

    def eliminar_pac(self):
        iden=self.id_eliminar.text()
        r=self.vetController.eliminar_pac(iden)
        self.abrir_ventana_menu()
        # if r==True:
        #     msgBox = QMessageBox()
        #     msgBox.setIcon(QMessageBox.information)
        #     msgBox.setText("Se elimino conrrectamente ")
            
#Implementacion 
    
def main(): 
    app=QApplication(sys.argv)
    mi_vista2=ventanaLogin()
    mi_vista2.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
    