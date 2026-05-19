from src.models.UserModel import UsuarioModel

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
    def recuperar_password(self, correo, nueva_password):

        return self.model.recuperar_password(
        correo,
        nueva_password
    )
    
    def login(self, email, contraseña):
        user = self.model.validar_login(email, contraseña)

        if user:
            return user, "Login correcto"

        return None, "Correo o contraseña incorrectos"
    def registrar(self, nombre, correo, contrasena):

        return self.model.registrar_usuario(
        nombre,
        correo,
        contrasena
    )
    
    def registrar_usuario(self, nombre, email, contraseña):
        success = self.model.registrar(nombre, email, contraseña)

        if success:
            return True, "Usuario creado correctamente"

        return False, "No se pudo registrar el usuario"
    
def registrar(self, nombre, correo, contrasena):

    return self.model.registrar_usuario(
        nombre,
        correo,
        contrasena
    ) 
      