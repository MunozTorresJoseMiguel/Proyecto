from models.UserModel import UsuarioModel

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def login(self, email, contraseña):
        user = self.model.validar_login(email, contraseña)

        if user:
            return user, "Login correcto"

        return None, "Correo o contraseña incorrectos"

    def registrar_usuario(self, nombre, email, contraseña):
        success = self.model.registrar(nombre, email, contraseña)

        if success:
            return True, "Usuario creado correctamente"

        return False, "No se pudo registrar el usuario"