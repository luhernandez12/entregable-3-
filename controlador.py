from modelo import* 

class login_controlador:
    def __init__(self, login_model:object = LoginModelo()):
        self.user_model = login_model
        
    def log_in(self, username:str, password:str):
        result = self.user_model.exists(username, password)
        return result

class sistema_controlador:
    def __init__(self, model = Sistema()):
        self.model = model

    def asignar_paciente(self,n,a,e,i):
        return self.model.asignar_paciente(n,a,i,e)
    
    def buscar_paciente(self, nombre):
        return self.model.buscar_eliminar(nombre)
    
    def delPets(self, id:str):
        return self.vet_model.delete_pet(id)



