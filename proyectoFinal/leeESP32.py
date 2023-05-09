from alarma import Alarma
import datetime
from llegadaAutoridades import LlegadaAutoridades
from persistenciaBD import PersistenciaBD
from persistenciaException import PersistenciaException
import random
import serial

BAUD_RATE = 115200
esp32 = serial.Serial('COM4', BAUD_RATE, timeout=1)
persistencia = PersistenciaBD()
oficiales = ['Armando López', 'Omar García',
             'Jesús Alatorre', 'Ricardo Jimenez', 'Mario Gonzalez']
alarma = None

while (True):
    data = esp32.readline()[:-2]

    if (data):
        sdata = data.decode('utf-8')
        print(sdata)

        if (sdata == 'Alarma encendida'):
            try:
                persistencia.agregaAlarma(
                    Alarma(0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            except PersistenciaException as pe:
                print()
                print(pe.msj)
                print(pe.cause)
        elif (sdata == 'Alarma desarmada'):
            try:
                alarmas = persistencia.consultaAlarmas()
                alarma = alarmas[-1]

                persistencia.agregaLlegada(LlegadaAutoridades(0, random.choice(
                    oficiales), datetime.datetime.now().strftime("%H:%M:%S"), alarma))
            except PersistenciaException as pe:
                print()
                print(pe.msj)
                print(pe.cause)
