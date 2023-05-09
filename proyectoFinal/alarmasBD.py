from alarma import Alarma
import mysql.connector
from persistenciaException import PersistenciaException
from tabla import Tabla


class AlarmasBD(Tabla):

    def __init__(self, user: str, password: str, host: str, database: str, nomTablaAlarmas: str):
        super().__init__(user, password, host, database)
        self.__nomTablaAlarmas = nomTablaAlarmas

    def agrega(self, alarma: Alarma):
        operacion = f"INSERT {self.__nomTablaAlarmas}"
        operacion += f" SET dia_hora = '{alarma.diaHora}';"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error: {self.msj_error(e)} en la tabla {self.__nomTablaAlarmas} de la base de datos {self._database}') from e

    def lista(self):
        listaAlarmas = []

        operacion = f"SELECT * FROM {self.__nomTablaAlarmas};"

        try:
            renglones = super().consulta(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error: {self.msj_error(e)} en la tabla {self.__nomTablaAlarmas} de la base de datos {self._database}') from e

        for renglon in renglones:
            alarma = Alarma(*renglon)
            listaAlarmas.append(alarma)

        return listaAlarmas
