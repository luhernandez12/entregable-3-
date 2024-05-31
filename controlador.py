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

    def newPet(self, data:dict):
        return self.vet_model.add_pet(data)
    
    def getPets(self, initName:str = ''):
        return self.vet_model.search_pets(initName)
    
    def delPets(self, id:str):
        return self.vet_model.delete_pet(id)



