from alarma import Alarma
from alarmasBD import AlarmasBD
import datetime
from llegadaAutoridades import LlegadaAutoridades
from llegadasAutoridadesBD import LlegadasAutoridadesBD
from persistenciaException import PersistenciaException


class PersistenciaBD:

    def __init__(self):
        self.__user = 'root'
        self.__password = 'Luisgon10$'
        self.__host = 'localhost'
        self.__database = 'joyeria'

        self.__alarmasBD = AlarmasBD(
            self.__user, self.__password, self.__host, self.__database, 'alarmas')
        self.__llegadasAutoridadesBD = LlegadasAutoridadesBD(
            self.__user, self.__password, self.__host, self.__database, 'llegadas_autoridades', 'alarmas')

    def agregaAlarma(self, alarma: Alarma):
        self.__alarmasBD.agrega(alarma)

    def consultaAlarmas(self):
        return self.__alarmasBD.lista()

    def agregaLlegada(self, llegadaAutoridades: LlegadaAutoridades):
        self.__llegadasAutoridadesBD.agrega(llegadaAutoridades)

    def consultaLlegadas(self):
        return self.__llegadasAutoridadesBD.lista()


if (__name__ == '__main__'):
    persistencia = PersistenciaBD()
    try:
        listaLlegadas = persistencia.consultaLlegadas()

        for llegada in listaLlegadas:
            print(llegada)
    except PersistenciaException as pe:
        print(pe.msj)
        print(pe.cause)
