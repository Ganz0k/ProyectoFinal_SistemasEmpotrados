import datetime


class Alarma:

    def __init__(self, idAlarma: int, diaHora: datetime.datetime) -> None:
        self.__idAlarma = idAlarma
        self.__diaHora = diaHora

    @property
    def idAlarma(self):
        return self.__idAlarma

    @idAlarma.setter
    def idAlarma(self, idAlarma: int):
        self.__idAlarma = idAlarma

    @property
    def diaHora(self):
        return self.__diaHora

    @diaHora.setter
    def diaHora(self, diaHora: datetime.datetime):
        self.__diaHora = diaHora

    def __str__(self):
        return f'{self.__idAlarma}, {self.__diaHora}'

    def __repr__(self):
        return f'{self.__class__.__module__}, {self.__class__.__name__}, {self.__idAlarma}, {self.__diaHora}'


if (__name__ == '__main__'):
    alarma = Alarma(15, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    print(alarma)
