class PersistenciaException(Exception):
    """Excepción lanzada cuando ocurre un error en el mecanismo de persistencia
    en el programa
    """

    def __init__(self, msj: str):
        """Constructor que inicializa los atributos de la clase

        -------------------------------------------------------
        Parameters
        ----------
        msj: str
            Mensaje que se mostrará con la excepción
        """
        super().__init__(msj)
        self.__msj = msj

    @property
    def msj(self):
        """Regresa el mensaje de la excepción

        @returns El mensaje de la excepción
        """
        return self.__msj

    @property
    def cause(self):
        """Regresa la causa original de la excepción

        @returns La causa original de la excepción
        """
        return self.__cause__

    def __str__(self):
        """Regresa una cadena con una representación amigable de la clase.

        ------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación amigable de la clase
        """
        return (f'PersistenciaException: {self.__msj}, {self.__cause__}')

    def __repr__(self):
        """Regresa una cadena con una representación no ambigua de la clase.

        --------------------------------------------------------------------
        Returns
        -------
        str
            Cadena con una representación no ambigua de la clase
        """
        return (f'{self.__module__}.{self.__class__.__name__}: {self.__msj}, {self.__cause__}')


if (__name__ == '__main__'):
    try:
        # Se lanza una excepcion del tipo PersistenciaException
        raise PersistenciaException('Error en el mecanismo de persistencia')
    except PersistenciaException as q:
        print(f'Tipo de excepción atrapada:  {q.__class__}')
        print()
        print(f'Descripcion amigable de la excepcion: {q.__str__()}')
        print()
        print(f'Descripcion unica de la excepcion: {q.__repr__()}')
        print()
        print(f'Descripcion de la excepcion: {q}')
        print()
        print(f'Argumentos del constructor de la excepcion: {q.args}')
        print()
        print(f'Mensaje de error: {q.msj} ')
        print(
            f'Si es una excepcion encadenada, causa original de la excepcion: {q.__cause__}')
        print()
