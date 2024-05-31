from modelo import* 

class login_controlador:
    def __init__(self, login_model:object = LoginModelo()):
        self.user_model = login_model
        
    def log_in(self, username:str, password:str):
        result = self.user_model.exists(username, password)
        return result





