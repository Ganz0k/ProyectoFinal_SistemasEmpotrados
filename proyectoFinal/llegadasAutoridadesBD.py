from alarma import Alarma
from llegadaAutoridades import LlegadaAutoridades
import mysql.connector
from persistenciaException import PersistenciaException
from tabla import Tabla


class LlegadasAutoridadesBD(Tabla):

    def __init__(self, user: str, password: str, host: str, database: str, nomTablaLlegadasAutoridades: str, nomTablaAlarmas: str):
        super().__init__(user, password, host, database)
        self.__nomTablaLlegadasAutoridades = nomTablaLlegadasAutoridades
        self.__nomTablaAlarmas = nomTablaAlarmas

    def agrega(self, llegadaAutoridades: LlegadaAutoridades):
        operacion = f"INSERT {self.__nomTablaLlegadasAutoridades}"
        operacion += f" SET nombre_oficial = '{llegadaAutoridades.nombreOficial}'"
        operacion += f", hora = '{llegadaAutoridades.hora}'"
        operacion += f", id_alarma = '{llegadaAutoridades.alarma.idAlarma}';"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error: {self.msj_error(e)} en la tabla {self.__nomTablaLlegadasAutoridades} de la base de datos {self._database}') from e

    def lista(self):
        llegadasAutoridades = []

        operacion = f"SELECT a.id_alarma, a.dia_hora, la.id_llegada_autoridades, la.nombre_oficial, la.hora"
        operacion += f" FROM {self.__nomTablaLlegadasAutoridades} AS la INNER JOIN {self.__nomTablaAlarmas} AS a"
        operacion += f" ON la.id_alarma = a.id_alarma;"

        try:
            renglones = super().consulta(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(
                f'Error: {self.msj_error(e)} en la tabla {self.__nomTablaLlegadasAutoridades} de la base de datos {self._database}') from e

        for idAlarma, diaHora, idLlegadaAutoridades, nombreOficial, hora in renglones:
            alarma = Alarma(idAlarma, diaHora)
            llegada = LlegadaAutoridades(
                idLlegadaAutoridades, nombreOficial, hora, alarma)

            llegadasAutoridades.append(llegada)

        return llegadasAutoridades
