import mysql.connector
import mysql.connector.errorcode


class Tabla:

    def __init__(self, user: str, password: str, host: str, database: str):
        self._user = user
        self._password = password
        self._host = host
        self._database = database

    def consulta(self, operacion: str):
        conexion = mysql.connector.connect(
            user=self._user, password=self._password, host=self._host, database=self._database)

        try:
            cursor = conexion.cursor()
            cursor.execute(operacion)
            resultados = cursor.fetchall()
            return resultados
        finally:
            if (conexion.is_connected()):
                cursor.close()
                conexion.close()

    def actualiza(self, operacion: str):
        conexion = mysql.connector.connect(
            user=self._user, password=self._password, host=self._host, database=self._database)

        try:
            cursor = conexion.cursor()
            cursor.execute(operacion)
            conexion.commit()
        except mysql.connector.IntegrityError:
            conexion.rollback()
            raise
        finally:
            if (conexion.is_connected()):
                cursor.close()
                conexion.close()

    def msj_error(self, err):
        if (err.errno == mysql.connector.errorcode.ER_SYNTAX_ERROR):
            return f'Error de sintaxis en la operacion'
        elif (err.errno == mysql.connector.errorcode.ER_DUP_ENTRY):
            return f'Registro repetido'
        elif (err.errno == mysql.connector.errorcode.ER_ROW_IS_REFERENCED_2):
            return f'No se puede actualizar o borrar registro'
        elif (err.errno == mysql.connector.errorcode.ER_NO_REFERENCED_ROW_2):
            return f'No se puede agregar o actualizar registro'
        elif (err.errno == mysql.connector.errorcode.ER_PARSE_ERROR):
            return f'Error de sintaxis en la operacion'
