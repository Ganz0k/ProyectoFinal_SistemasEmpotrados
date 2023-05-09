from alarma import Alarma
from llegadaAutoridades import LlegadaAutoridades
from persistenciaBD import PersistenciaBD
from persistenciaException import PersistenciaException
from tkinter import *
from tkinter import ttk


class Aplicacion:

    def __init__(self):
        self.persistencia = PersistenciaBD()
        self.raiz = Tk()
        self.raiz.geometry('1000x500')
        self.raiz.title('Joyería')

        self.lblTitulo = ttk.Label(
            self.raiz, text='Registros de veces que la alarma sonó y de las llegadas de las autoridades', font=(None, 20))
        self.lblTitulo.pack(side=TOP)

        self.genText = Text(self.raiz, width=110, height=20)
        self.genText.pack(side=TOP)

        self.botonAlarmas = ttk.Button(
            self.raiz, text='Ver alarmas', command=self.obtenerAlarmas)
        self.botonAlarmas.pack(side=LEFT)

        self.botonLlegadas = ttk.Button(
            self.raiz, text='Ver llegadas autoridades', command=self.obtenerLlegadas)
        self.botonLlegadas.pack(side=RIGHT)

        self.raiz.mainloop()

    def obtenerAlarmas(self):
        self.genText.delete('1.0', END)
        texto = 'ID alarma | Día y hora\n'
        texto += '----------|-----------\n'

        try:
            listaAlarmas = self.persistencia.consultaAlarmas()

            for alarma in listaAlarmas:
                texto += f'{alarma.idAlarma}         | {alarma.diaHora}\n'

            self.genText.insert('1.0', texto)
        except PersistenciaException as pe:
            print(pe.msj)
            print(pe.cause)

    def obtenerLlegadas(self):
        self.genText.delete('1.0', END)
        texto = 'ID llegada | Nombre del oficial | Día y hora de alarma | Hora de llegada\n'
        texto += '-----------|--------------------|----------------------|----------------\n'

        try:
            listaLlegadas = self.persistencia.consultaLlegadas()

            for llegada in listaLlegadas:
                texto += f'{llegada.idLlegadaAutoridades}          | {llegada.nombreOficial}    | {llegada.alarma.diaHora}  | {llegada.hora}\n'

            self.genText.insert('1.0', texto)
        except PersistenciaException as pe:
            print(pe.msj)
            print(pe.cause)


def main():
    app = Aplicacion()


if (__name__ == '__main__'):
    main()
