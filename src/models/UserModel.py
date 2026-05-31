import bcrypt
from .databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, nombre, email, contraseña):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(contraseña.encode('utf-8'), salt)

        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, email, contraseña) VALUES (%s, %s, %s)",
                (nombre, email, hashed_pw.decode('utf-8'))
            )
            conn.commit()
            return True

        except Exception as e:
            print(f"Error: {e}")
            return False

        finally:
            conn.close()

    def validar_login(self, correo, contrasena):

        conn = Database.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT * FROM usuarios
        WHERE correo = %s
        """

        cursor.execute(query, (correo,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            
         if bcrypt.checkpw(
            contrasena.encode("utf-8"),
            user["contrasena"].encode("utf-8")
        ):

            return user

        return None
    
    def recuperar_password(self, correo, nueva_password):

        conn = Database.get_connection()
        cursor = conn.cursor()

        hashed_password = bcrypt.hashpw(
                nueva_password.encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")

        query = """
            UPDATE usuarios
        SET contrasena = %s
            WHERE correo = %s
            """

            
        cursor.execute(
                query,
                (hashed_password, correo)
        )  

        conn.commit()

        cursor.close()
        conn.close()

        return True, "Contraseña actualizada"

    
    
    
    
    def registrar_usuario(self, nombre, correo, contrasena):

        conn = Database.get_connection()
        cursor = conn.cursor()

        verificar = """
        SELECT * FROM usuarios
        WHERE correo = %s
        """

        cursor.execute(verificar, (correo,))
        existe = cursor.fetchone()

        if existe:

            cursor.close()
            conn.close()

            return False, "El correo ya existe"

        query = """
        INSERT INTO usuarios
        (nombre, correo, contrasena)
        VALUES (%s, %s, %s)
        """

        hashed_password = bcrypt.hashpw(
        contrasena.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")
        
        cursor.execute(
        query,
        (nombre, correo, hashed_password)
    )

        conn.commit()

        cursor.close()
        conn.close()

        return True, "Usuario registrado correctamente"