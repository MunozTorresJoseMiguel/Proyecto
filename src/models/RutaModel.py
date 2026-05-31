from .databaseModel import Database

class RutaModel:

    def buscar_rutas_por_parada(self, texto):

        conn = Database.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT DISTINCT r.*
        FROM rutas r
        INNER JOIN recorrido_ruta rr
            ON r.id_ruta = rr.id_ruta
        INNER JOIN paradas p
            ON rr.id_parada = p.id_parada
        WHERE p.nombre_parada LIKE %s
        """

        cursor.execute(
            query,
            (f"%{texto}%",)
        )

        rutas = cursor.fetchall()

        cursor.close()
        conn.close()

        return rutas