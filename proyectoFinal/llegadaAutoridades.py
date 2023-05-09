from alarma import Alarma
import datetime


class LlegadaAutoridades:

    def __init__(self, idLlegadaAutoridades: int, nombreOficial: str, hora: datetime.datetime, alarma: Alarma) -> None:
        self.__idLlegadaAutoridades = idLlegadaAutoridades
        self.__nombreOficial = nombreOficial
        self.__hora = hora
        self.__alarma = alarma

    @property
    def idLlegadaAutoridades(self):
        return self.__idLlegadaAutoridades

    @idLlegadaAutoridades.setter
    def idLlegadaAutoridades(self, idLlegadaAutoridades: int):
        self.__idLlegadaAutoridades = idLlegadaAutoridades

    @property
    def nombreOficial(self):
        return self.__nombreOficial

    @nombreOficial.setter
    def nombreOficial(self, nombreOficial: str):
        self.__nombreOficial = nombreOficial

    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, hora: datetime.datetime):
        self.__hora = hora

    @property
    def alarma(self):
        return self.__alarma

    @alarma.setter
    def alarma(self, alarma: Alarma):
        self.__alarma = alarma

    def __str__(self):
        return f'{self.__idLlegadaAutoridades}, {self.__nombreOficial}, {self.__hora}, {self.__alarma}'

    def __repr__(self):
        return f'{self.__class__.__module__}, {self.__class__.__name__}, {self.__idLlegadaAutoridades}, {self.__nombreOficial}, {self.__hora}, {self.__alarma}'


if (__name__ == '__main__'):
    alarma = Alarma(15, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    llegada = LlegadaAutoridades(
        5, 'Glen Gallegos', datetime.datetime.now().strftime('%H:%M:%S'), alarma)

    print(llegada)
