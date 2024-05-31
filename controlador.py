from modelo import* 

class login_controlador:
    def __init__(self, login_model:object = LoginModelo()):
        self.user_model = login_model
        
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



