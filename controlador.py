from modelo import* 

#Clase controlador 
class login_controlador:
    def __init__(self):
        self.user_model=LoginModelo()
        
    def log_in(self, username:str, password:str):
        result = self.user_model.existe(username, password)
        return result

#Clase sistema
class sistema_controlador:
    def __init__(self, model = Sistema()):
        self.model = model

    def asignar_paciente(self,n,a,e,i):
        return self.model.asignar_paciente(n,a,i,e)
    
    def buscar_paciente(self, nombre):
        return self.model.buscar_eliminar(nombre)
    
    def eliminar_pac(self, id):
        return self.model.eliminar_paciente(id)



