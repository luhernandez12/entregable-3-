from vista import* 
from modelo import* 

class login_controlador:
    def __init__(self, login_model:object = LoginModelo()):
        self.user_model = login_model_model
        
    def log_in(self, username:str, password:str):
        result = self.user_model.exists(username, password)
        return result

class Coordinador:
    def __init__(self,vista,modelo):
        self.__miVista = vista
        self.__miModelo = modelo
    
    def recibirLogin(self, user, password):
        self.__miModelo.entrada(usuario,clave)
    def recibiInfo(self,n, a, i, e):
        self.__miModelo.asignar_paciente(n, a, i, e)

    # def eliminarPaciente(nombre):
    #     self.__miModelo()

app=QApplication(sys.argv)
mi_vista=ventanaPrincipal()
mi_modelo=Sistema("almacenamiento.db")
mi_controlador=Coordinador(mi_vista,mi_modelo)
mi_vista.setCoordinador(mi_controlador)
mi_vista.show()
sys.exit(app.exec_())

